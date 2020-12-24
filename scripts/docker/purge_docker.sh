#!/bin/bash

# Purge docker
docker system prune
docker system prune --volumes

# Delete all containers
docker rm $(docker ps -a -q) --force

# Delete all images
docker rmi $(docker images -q) --force

# Remove rest of volumes
cd ..

sudo rm -rf mysql/persistence
