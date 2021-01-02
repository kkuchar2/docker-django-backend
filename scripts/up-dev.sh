#!/bin/bash

./unlock_db_volume.sh

docker-compose -f ../api/docker-compose-dev.yml up --build
