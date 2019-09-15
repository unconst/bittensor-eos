import bittensor

from concurrent import futures
import grpc
from loguru import logger
import pickle
import time
from threading import Lock

class Buffer:
    def __init__(self,  sender_id = None,
                        message_id = None,
                        create_time = None,
                        lspikes = None,
                        uspikes = None,
                        dspikes = None,
                        lgrads = None):

        self.sender_id = sender_id
        self.message_id = message_id
        self.create_time = create_time
        self.lspikes = lspikes
        self.uspikes = uspikes
        self.dspikes = dspikes
        self.lgrads = lgrads

    def set(self, sender_id = None,
                  message_id = None,
                  create_time = None,
                  lspikes = None,
                  uspikes = None,
                  dspikes = None,
                  lgrads = None ):

        if not self.sender_id:
            self.sender_id = sender_id
        if not self.message_id:
            self.message_id = message_id
        if not self.create_time:
            self.create_time = create_time
        if not self.lspikes:
            self.lspikes = lspikes
        if not self.uspikes:
            self.uspikes = uspikes
        if not self.dspikes:
            self.dspikes = dspikes
        if not self.lgrads:
            self.lgrads = lgrads


class Neuron(bittensor.proto.bolt_pb2_grpc.BoltServicer):

    def __init__(self, config, dendrite, nucleus, metagraph):
        self.config = config
        self.dendrite = dendrite
        self.nucleus = nucleus
        self.metagraph = metagraph
        self.mem_lock = Lock()
        self.memory = {}

        # Init server.
        self.server_address = self.config.bind_address + ":" + self.config.port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        bittensor.proto.bolt_pb2_grpc.add_BoltServicer_to_server(self, self.server)
        self.server.add_insecure_port(self.server_address)

    def __del__(self):
        self.server.stop(0)
        logger.debug('Stopped Serving Neuron at: {}.', self.server_address)

    def serve(self):
        self.server.start()
        logger.debug('Started Serving Neuron at: {}.', self.server_address)

    def Spike(self, request, context):
        # Unpack message.
        sender_id = request.sender_identity
        message_id = request.message_identity
        uspikes = pickle.loads(request.payload)

        # Check for repsonse in buffer.
        if message_id in self.memory:
            # Return local spikes.
            return self.memory[message_id].lspikes

        # Get downstream spikes.
        dspikes = self.dendrite.spike(message_id, uspikes)

        # Get local spikes.
        lspikes = self.nucleus.spike(uspikes, dspikes)

        # Save to buffer.
        self.mem_lock.acquire()
        try:
            self.memory[message_id] = Buffer(
                                          sender_id = sender_id,
                                          message_id = message_id,
                                          create_time = time.time(),
                                          lspikes = lspikes,
                                          uspikes = uspikes,
                                          dspikes = dspikes)
        finally:
            self.mem_lock.release()


        # Pack response.
        payload = pickle.dumps(lspikes, protocol=0)
        response = bittensor.proto.bolt_pb2.SpikeResponse(
                        responder_identity = self.config.identity,
                        message_identity = message_id,
                        payload = payload)

        return response


    def Grade(self, request, context):
        # Unpack request.
        sender_id = request.sender_identity
        message_id = request.message_identity
        ugrades = pickle.loads(request.payload)

        # Check for lost or badly routed grades.
        if message_id not in self.memory:
            return

        # Get local spikes.
        mem_buffer = self.memory[message_id]
        lspikes = mem_buffer.lspikes

        # Get downstream spikes.
        dspikes = mem_buffer.dspikes

        # Get upstream spikes
        uspikes = mem_buffer.uspikes

        # Get downstream grads and local grads.
        dgrades, lgrads = self.nucleus.grade(ugrades, uspikes, dspikes)

        # Set lgrades in buffer.
        mem_buffer.lgrads = lgrads

        # Send downstream grads.
        self.dendrite.grade(message_id, dgrades)

        return bittensor.proto.bolt_pb2.GradeResponse(accept=True)

    def Learn (self):
        # Function clears the message buffer of all outdated memory objects
        # and applies gradients from memory.
        logger.info('Learn.')

        # Requires lock because this thread contains multiple
        # read and write operations.
        self.mem_lock.acquire()
        try:
            mem_size = len(self.memory)
            logger.info('Mem size: {}', mem_size)

            # Apply batch and clean memory of lingering objects.
            to_delete = []
            time_now = time.time()
            for message_id in self.memory.keys():
                row = self.memory[message_id]

                # Check if row has ready gradients.
                if row.lgrads is not None:
                    to_delete.append(message_id)
                    self.nucleus.learn(row.lgrads)

                # Delete lingering objects.
                elif (time_now - row.create_time) > self.config.time_till_expire:
                    to_delete.append(message_id)

            # Delete batch and lingering objects.
            for msg_id in to_delete:
                del self.memory[msg_id]

        except Exception as e:
            logger.error('Neuron failed Learn with error: '+ str(e))

        finally:
            self.mem_lock.release()
