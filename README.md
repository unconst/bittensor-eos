## BitTensor Network Daemon

<img src="assets/mycellium.jpeg" width="1000" />

---

## Overview

BitTensor is neural network which trains across computers in a peer-to-peer fashion. In absence of centralized control, the network uses collaborative filtering to select computers with high informational significance. To these computers the network mints digital tokens which provide power over the network.

This repo contains an implementation of a peer in this network. It trains a self-supervised language representation using a dumpy corpus of text by taking as input the output of its peers in the network. In doing so, it mines the network native digital token.

For an in-depth description of this software, see https://www.bittensor.com/learn

---
## Run Locally
```
$ git clone https://github.com/unconst/BitTensor & cd BitTensor

# Start EOS chain.
$ ./start_eos.sh  

# Start node 1.
$ ./bittensor.sh

# Start node 2.
$ ./bittensor.sh
```
**Note**: This script uses upnpc to punch a hole in your router. If that fails, you will need to login to your router and do so manually.

---

## Learn More

Read the [paper](https://www.bittensor.com/learn) or join our [slack](https://bittensor.slack.com/)

---

## Pull Requests

This is alpha software, so in the interest of speed, just directly commit to the repo. To make that feasible, try to keep your work as modular as possible. I like to iterate fast by creating another sub project where tests can grow. For instance, in this repo, the sync_kgraph, and async_kgraph are separate independent implementations. Yes this creates code copying and rewrite, but allows fast development.

Also, use [Yapf](https://github.com/google/yapf) for code formatting. You can run the following to format before a commit.
```
$ pip install yapf
$ yapf --style google -r -vv -i .
```

---

## License

MIT
