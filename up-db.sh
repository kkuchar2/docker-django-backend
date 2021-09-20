#!/bin/bash

source "up-common.sh"

CONFIG_FILE=/home/"$USER"/config/.env.dev
COMPOSE_FILE=docker-compose-db.yml

REQUIRED_VARIABLES=(
    'MYSQL_ROOT_PASSWORD'
    'MYSQL_USER'
    'MYSQL_PASSWORD'
    'MYSQL_DATABASE'
)

check_file_exists "$COMPOSE_FILE"
check_file_exists "$CONFIG_FILE"

echoF
echo "-> Compose file: $COMPOSE_FILE"
echo "-> Config file: $CONFIG_ILE"

validate_configuration_file "${CONFIG_FILE}" "${REQUIRED_VARIABLES}"

stop_container db_container

echo
echo "docker-compose --env-file $CONFIG_FILE --file $COMPOSE_FILE up --build"
echo

docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build
