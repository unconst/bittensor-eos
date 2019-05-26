# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto.tensorflow.core.framework import tensor_pb2 as proto_dot_tensorflow_dot_core_dot_framework_dot_tensor__pb2


class BoltStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Spike = channel.unary_unary(
        '/Bolt/Spike',
        request_serializer=proto_dot_tensorflow_dot_core_dot_framework_dot_tensor__pb2.TensorProto.SerializeToString,
        response_deserializer=proto_dot_tensorflow_dot_core_dot_framework_dot_tensor__pb2.TensorProto.FromString,
        )


class BoltServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Spike(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BoltServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Spike': grpc.unary_unary_rpc_method_handler(
          servicer.Spike,
          request_deserializer=proto_dot_tensorflow_dot_core_dot_framework_dot_tensor__pb2.TensorProto.FromString,
          response_serializer=proto_dot_tensorflow_dot_core_dot_framework_dot_tensor__pb2.TensorProto.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Bolt', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
