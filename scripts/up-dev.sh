#!/bin/bash

echo "Stopping containers..."

docker container stop django_container
docker container stop redis_container
docker container stop db_container

./unlock_api_persistence.sh

docker-compose -f ../api/docker-compose-dev.yml up --build
