#!/bin/bash

source "up-common.sh"

CONFIG_FILE=/home/"$USER"/config/.env.prod
COMPOSE_FILE=docker-compose-prod.yml
REQUIRED_VARIABLES=(
    'SECRET_KEY'
    'MASTER_EMAIL'
    'MASTER_PASSWORD'
    'MYSQL_DATABASE'
    'MYSQL_USER'
    'MYSQL_PASSWORD'
    'MYSQL_HOST'
    'MYSQL_PORT'
    'EMAIL_HOST_USER'
    'EMAIL_HOST_PASSWORD'
    'GS_CREDENTIALS_JSON'
    'GS_PROJECT_ID'
    'GS_BUCKET_NAME'
    'SENTRY_DSN_URL'
)

check_file_exists "$COMPOSE_FILE"
check_file_exists "$CONFIG_FILE"

echo
echo "-> Compose file: $COMPOSE_FILE"
echo "-> Config file: $CONFIG_FILE"

validate_configuration_file "${CONFIG_FILE}" "${REQUIRED_VARIABLES}"

unlock_api_persistence

stop_container django_container

echo
echo "docker-compose --env-file $CONFIG_FILE --file $COMPOSE_FILE up --build"
echo

docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build
