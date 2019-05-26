import collections
import math
from matplotlib import pylab
import numpy as np
import random
from sklearn.manifold import TSNE
import tensorflow as tf
import time
import threading
import zipfile


_ONE_DAY_IN_SECONDS = 60*60*24

class Neuron():
    def __init__(self, dendrite):
        self.dendrite = dendrite
        self.train_thread = threading.Thread(target=self._train)
        self.train_thread.setDaemon(True)
        self.running = False
        self.mutex = threading.Lock()

        # Dataset zip file.
        self.filename = 'text8.zip'
        # Size of vocab embedding.
        self.vocabulary_size = 50000
        # Size of training batch.
        self.batch_size = 128
        # Dimension of the embedding vector.
        self.embedding_size = 128
        # Number of negative examples to sample.
        self.num_sampled = 64
      
        # Build Dataset.
        self.build_vocabulary()

        # Build Graph.
        self.graph = tf.Graph()
        with self.graph.as_default(), tf.device('/cpu:0'):
            self.build_graph()

        # Create TF Session.
        self.session = tf.Session(graph=self.graph)

    def build_vocabulary(self):

        print ('Building vocabulary...')
        # Read textfile.
        f = zipfile.ZipFile(self.filename)
        for name in f.namelist():
            self.words = tf.compat.as_str(f.read(name)).split()
        f.close()

        counts = [('UNK', -1)]
        counts.extend(collections.Counter(self.words).most_common(self.vocabulary_size - 1))
        self.string_map = [c[0] for c in counts]

        #print (self.string_map)
        print ('done. \n')

    def build_graph(self):

        # Build Graph.
        print ('Building graph...')
    
        # Input words.
        self.batch_words = tf.reshape((tf.placeholder(tf.string, shape=[None, 1])), [-1])
        word_ids = tf.contrib.lookup.string_to_index(self.batch_words, mapping=tf.constant(self.string_map), default_value=0)

        # Input labels.
        self.batch_labels = tf.placeholder(tf.string, shape=[None, 1])
        label_ids = tf.contrib.lookup.string_to_index(self.batch_labels, mapping=tf.constant(self.string_map), default_value=0)

        # Embeddings Lookup.
        embeddings = tf.Variable(tf.random_uniform([self.vocabulary_size, self.embedding_size], -1.0, 1.0))
        word_embeddings = tf.nn.embedding_lookup(embeddings, word_ids)
        
        # Remote features.
        remote_inputs = self.dendrite.spike(self.batch_words)

        # Hidden Layer
        l1 = tf.concat([word_embeddings, remote_inputs], axis=1)
        w1 = tf.Variable(tf.random_uniform([self.embedding_size*2, self.embedding_size], -1.0, 1.0))
        b1 = tf.Variable(tf.zeros([self.embedding_size]))
        self.output = tf.matmul(l1, w1) + b1

        # Embedding Weights
        softmax_weights = tf.Variable(tf.truncated_normal([self.vocabulary_size, self.embedding_size], stddev=1.0 / math.sqrt(self.embedding_size)))
        softmax_biases = tf.Variable(tf.zeros([self.vocabulary_size]))

        # Sampled Softmax Loss.
        batch_loss = tf.nn.sampled_softmax_loss(
            weights=softmax_weights,
            biases=softmax_biases,
            labels=label_ids,
            inputs=self.output,
            num_sampled=self.num_sampled,
            num_classes=self.vocabulary_size,
            num_true=1,
            sampled_values=None,
            remove_accidental_hits=True,
            partition_strategy='mod',
            name='sampled_softmax_loss',
            seed=None)

        # Average loss.
        self.loss = tf.reduce_mean(batch_loss)

        # Optimizer.
        self.optimizer = tf.train.AdagradOptimizer(1.0).minimize(self.loss)

        print ('done. \n')

    def start(self):
        self.running = True
        self.train_thread.start()

    def stop(self):
        self.running = False
        self.train_thread.join()

    def spike(self, batch_tensor):
        with self.mutex:
            feed_dict = {self.words : batch_tensor}
            return self.session.run(self.output, feed_dict={self.words : batch_tensor})

    def _train(self):
        print ('Training ...')
        with self.session:

            # Init.
            tf.global_variables_initializer().run()
            tf.tables_initializer().run()

            # Train loop.
            average_loss = 0
            step = -1
            while self.running:
                with self.mutex:
                    step += 1

                    # Build a random batch [feature = word_i, label = word_i+1]
                    batch_words = []
                    batch_labels = []
                    for i in range(self.batch_size):
                        index = random.randint(0, len(self.words) - 2)
                        batch_words.append(self.words[index])
                        batch_labels.append([self.words[index + 1]])

                    # Train Step.
                    feed_dict = {self.batch_words: batch_words, self.batch_labels: batch_labels}
                    _, l = self.session.run([self.optimizer, self.loss], feed_dict=feed_dict)
                    average_loss += l

                    # Progress notification.
                    if step % 2000 == 1 and step > 2000:
                        print('     Average loss at step %d: %f' % (step, average_loss/2000))
                        average_loss = 0

        print ('done. \n')





