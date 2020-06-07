echo "checking requirements"

# Test for python3
if [ -x python3 ]; then
  echo "You need to install python3: https://realpython.com/installing-python/"
  exit 0
fi

# Test for loguru
pip3 install loguru
pip3 install miniupnpc

# Test for docker
if [ -x "$(docker -v)" ]; then
  echo "You need to install docker: https://docs.docker.com/install/"
  exit 0
fi

if (! docker stats --no-stream ); then
  echo "You need to start the docker deamon"
  echo '$ sudo systemctl enable docker'
  echo '$ sudo groupadd docker'
  echo '$ sudo usermod -aG docker ${USER}'
  echo '$ su -s ${USER}'
fi
