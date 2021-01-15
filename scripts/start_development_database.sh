#!/bin/bash

# Remove old mysql persistence
sudo rm -rf ../db/persistence

# Up database
docker-compose -f ../db/docker-compose-dev.yml up -d
