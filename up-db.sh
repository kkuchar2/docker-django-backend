#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source "${DIR}/scripts/up-common.sh"

CONFIG_FILE=/home/"$USER"/config/.env.db.prod
COMPOSE_FILE=docker-compose-db.yml

REQUIRED_VARIABLES=(
    'MYSQL_EXTERNAL_PORT'
    'MYSQL_INTERNAL_PORT'
    'MYSQL_ROOT_PASSWORD'
    'MYSQL_USER'
    'MYSQL_PASSWORD'
    'MYSQL_DATABASE'
)

ensure_file_exists "$COMPOSE_FILE"
ensure_file_exists "$CONFIG_FILE"

echo
echo "-> Compose file: $COMPOSE_FILE"
echo "-> Config file: $CONFIG_ILE"

validate_configuration_file "${CONFIG_FILE}" "${REQUIRED_VARIABLES}"

stop_container db_container

echo
echo "docker-compose --env-file $CONFIG_FILE --file $COMPOSE_FILE up --build"
echo

docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build
