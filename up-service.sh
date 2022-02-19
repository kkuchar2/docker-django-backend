#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
COLUMNS=$(tput cols)
title="Welcome to Backend Service"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

dash_line() {
    printf '%*s\n' "$COLUMNS" '' | tr ' ' -
}

empty_line() {
    printf '\n'
}

centered_title() {
    printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title"
}

source "${DIR}/scripts/up-common.sh"

HELP_TEXT=\
"   USAGE:\n
    
    Help: -h, --help\n
    Attach service container: -a, --attach\n
    Specify environment: -e [dev/prod], --env [dev, prod]
"

attached=false
environment='dev'
create_db=false

if ! options=$(getopt -o ae:h\? -l attach,env:,help -- "$@")
then
    exit 1
fi

set -- $options

while [ $# -gt 0 ]
do
    case $1 in
    -e|--env) environment="$2" ; shift;;
    -a|--attach) attached=true ;;
    -db|--database) create_db=true ;;
    -h|--help|-\?) echo -e $HELP_TEXT; exit;;
    (--) shift; break;;
    (-*) echo "$0: error - unrecognized option $1" 1>&2; exit 1;;
    (*) break;;
    esac
    shift
done

REQUIRED_VARIABLES_MYSQL=(
    'MYSQL_HOST'
    'MYSQL_INTERNAL_PORT'
    'MYSQL_EXTERNAL_PORT'
    'MYSQL_DATABASE'
    'MYSQL_USER'
    'MYSQL_PASSWORD'
    'MYSQL_ROOT_PASSWORD'
)

REQUIRED_COMMON_VARIABLES=(
    'SECRET_KEY'
    'MASTER_EMAIL'
    'MASTER_PASSWORD'
    'EMAIL_HOST_USER'
    'EMAIL_HOST_PASSWORD'
    'DJANGO_INTERNAL_PORT'
    'DJANGO_EXTERNAL_PORT'
)

REQUIRED_VARIABLES_GS_STORAGE=(
    'GS_CREDENTIALS_JSON'
    'GS_PROJECT_ID'
    'GS_BUCKET_NAME'
)

# Apply common required variables for both environments
REQUIRED_VARIABLES_DEV=(${REQUIRED_COMMON_VARIABLES[@]})
REQUIRED_VARIABLES_PROD=(${REQUIRED_COMMON_VARIABLES[@]})

# Apply MySQL required variables for both environments
REQUIRED_VARIABLES_DEV+=(${REQUIRED_VARIABLES_MYSQL[@]})
REQUIRED_VARIABLES_PROD+=(${REQUIRED_VARIABLES_MYSQL[@]})

# Apply Google Storage required variables to Prod environment
REQUIRED_VARIABLES_PROD+=(${REQUIRED_VARIABLES_GS_STORAGE[@]})

CONFIG_FILE_DEV=/home/"$USER"/config/.env.dev
CONFIG_FILE_PROD=/home/"$USER"/config/.env.prod

COMPOSE_FILE_DEV=docker-compose-dev.yml
COMPOSE_FILE_PROD=docker-compose-prod.yml
COMPOSE_FILE_DB=docker-compose-db.yml

COMPOSE_FILE=$COMPOSE_FILE_DEV
CONFIG_FILE=$CONFIG_FILE_DEV
REQUIRED_VARIABLES=(${REQUIRED_VARIABLES_DEV[@]})

if [ "$environment" = "'prod'" ]; then
    COMPOSE_FILE=$COMPOSE_FILE_PROD
    CONFIG_FILE=$CONFIG_FILE_PROD
    REQUIRED_VARIABLES=(${REQUIRED_VARIABLES_PROD[@]})
fi

dash_line
empty_line
centered_title
empty_line
dash_line

echo "Environment: $environment"
echo "Attached: $attached"
echo "Compose file: $COMPOSE_FILE"
echo "Config file: $CONFIG_FILE"

dash_line

# Check if config file exists
ensure_file_exists $CONFIG_FILE

# Check if all required enviroment variables are set in config file
validate_configuration_file "${CONFIG_FILE}" "${REQUIRED_VARIABLES}"

# Unslock persistence directory content created by Docker
unlock_api_persistence

# Stop current running service container
stop_container django_container

# Stop current running database container
stop_container db_container

dash_line

if [[ $attached == false ]]; then
    echo "Deploying detached service"
    dash_line
    docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build --detach
else
    echo "Deploying attached service"
    dash_line
    docker-compose --env-file "$CONFIG_FILE" --file "$COMPOSE_FILE" up --build
fi
