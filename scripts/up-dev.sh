#!/bin/bash

function stop_container() {
    if [ "$(docker ps -q -f name="$1")" ]; then
        echo "Stopping container $1"
        docker container stop "$1"
    fi
}

function run_docker_compose() {
  echo
  echo "Running:"
  echo " -> Compose file: $2"
  echo " -> Config file: $1"
  echo

  if [ ! -f "$1" ]; then
    echo "Error: $1 not found. Exiting."
    exit 0
  fi

  if [ ! -f "$2" ]; then
    echo "Error: $2 not found. Exiting."
    exit 0
  fi

  echo "docker-compose --env-file $1 --file $2 up --build"
  echo

  docker-compose --env-file "$1" --file "$2" up --build
}

stop_container django_container
stop_container redis_container
stop_container db_container

./unlock_api_persistence.sh

run_docker_compose /home/"$USER"/config/.env.dev ../api/docker-compose-dev.yml
