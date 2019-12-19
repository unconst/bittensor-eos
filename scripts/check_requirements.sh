# Test for python3
if [ -x python3 ]; then
  echo "You need to install python3: https://realpython.com/installing-python/"
  exit 0
fi

# Test for loguru
if python3 -c "import package_name" &> /dev/null; then
  echo "You need to install loguru"
  pip3 install loguru
fi

# Test for docker
if [ -x "$(docker -v)" ]; then
  echo "You need to install docker: https://docs.docker.com/install/"
  exit 0
fi
