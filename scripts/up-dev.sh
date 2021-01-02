#!/bin/bash

./unlock_api_persistence.sh

docker-compose -f ../api/docker-compose-dev.yml up --build
