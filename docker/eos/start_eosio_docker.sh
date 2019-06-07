#!/usr/bin/env bash
set -o errexit

# change to script's directory
cd "$(dirname "$0")"

source constant.sh

# if [ -e "data/initialized" ]
# then
# script="./scripts/continue_blockchain.sh"
# else
script="./scripts/init_blockchain.sh"
# fi

echo "=== run docker container from the $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG image ==="
docker run --rm --name eosio_bittensor_container -d \
-p 8888:8888 -p 9876:9876 \
--mount type=bind,src="$(pwd)"/contracts,dst=/opt/eosio/bin/contracts \
--mount type=bind,src="$(pwd)"/scripts,dst=/opt/eosio/bin/scripts \
--mount type=bind,src="$(pwd)"/data,dst=/mnt/dev/data \
-w "/opt/eosio/bin/" $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG /bin/bash -c "$script"

if [ "$1" != "--nolog" ]
then
    echo "=== follow eosio_bittensor_container logs ==="
    docker logs eosio_bittensor_container --follow
fi