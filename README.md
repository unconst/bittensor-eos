## BitTensor Network Daemon

<img src="assets/mycellium.jpeg" width="1000" />

---

## Overview

BitTensor is a Machine Intelligence benchmark which rewards knowledge production from within a peer to peer network. In absence of centralized control, the network scores this knowledge collaboratively, having participants measure the informational significance of their peers. A digital ledger then mints tokens to those computer proportional these scores.

---
## Run Locally
1. Install [python3](https://realpython.com/installing-python/)
1. Install [Docker](https://docs.docker.com/install/)

```
$ git clone https://github.com/unconst/BitTensor & cd BitTensor

# Start EOS chain.
$ ./start_eos.sh  

# Start node 1.
$ ./bittensor.sh

# Start node 2.
$ ./bittensor.sh

# start tensorboard visualizer
$ ./start_visualizer.sh -e http://host.docker.internal:8888
```
---

## Installing Docker
```
# Follow these commands
1. Install docker: https://docs.docker.com/install/"

# Enable the Deamon
$ sudo systemctl enable docker'

# Create docker group.
$ sudo groupadd docker

# Add you user to the docker group.
$ sudo usermod -aG docker ${USER}

# Log out or run.
$ su -s ${USER}
```


## Learn More

Join our [slack](https://bittensor.slack.com/) and say hello :)

---

## Pull Requests

This is alpha software, so in the interest of speed, just directly commit to the repo and use [Yapf](https://github.com/google/yapf) for code formatting.
```
$ pip install yapf
$ yapf --style google -r -vv -i .
```

---

## License

MIT
