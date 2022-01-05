#!/bin/bash

source "up-common.sh"

CONFIG_FILE=/home/"$USER"/config/.env.dev
COMPOSE_FILE=docker-compose-dev.yml

REQUIRED_VARIABLES=(
    'MYSQL_EXTERNAL_PORT'
    'MYSQL_INTERNAL_PORT'
    'MYSQL_ROOT_PASSWORD'
    'MYSQL_USER'
    'MYSQL_PASSWORD'
    'MYSQL_DATABASE'
    'SECRET_KEY'
    'EMAIL_HOST_PASSWORD'
    'EMAIL_HOST_USER'
    'MASTER_EMAIL'
    'MASTER_PASSWORD'
    'DJANGO_INTERNAL_PORT'
    'DJANGO_EXTERNAL_PORT'
)

check_file_exists "$COMPOSE_FILE"
check_file_exists "$CONFIG_FILE"

echo
echo "-> Compose file: $COMPOSE_FILE"
echo "-> Config file: $CONFIG_FILE"

validate_configuration_file "${CONFIG_FILE}" "${REQUIRED_VARIABLES}"

unlock_api_persistence

stop_container django_container
stop_container db_container

echo
echo "docker-compose --env-file $CONFIG_FILE --file $COMPOSE_FILE up --build"
echo

docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build
