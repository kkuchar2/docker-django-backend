#!/bin/bash
function set_variable() {
  env_variable=$1
  target_value=$2
  if [[ -z "${!env_variable}" ]]; then
    export "$env_variable"="$target_value"
    printf "  $%s\t| (default) \t|  %s \n" "$env_variable" "${!env_variable}" | expand -t 25
  else
    printf "  $%s\t| (already set) \t|  %s \n" "$env_variable" "${!env_variable}" | expand -t 25
  fi
}

printf "\n"
printf "..................................................................................\n"
printf "Config name\t|  State\t|  Value\n" | expand -t 25
printf "..................................................................................\n"
set_variable "MYSQL_ROOT_PASSWORD" "root"
set_variable "MYSQL_USER" "root"
set_variable "MYSQL_PASSWORD" "root"
set_variable "MYSQL_DATABASE" "klkuch_db"
set_variable "DJANGO_SECRET" "$(base64 /dev/urandom | head -c50)"
set_variable "PYTHON_BUFFERED" 1
printf "..................................................................................\n"
printf "\n"

docker-compose up -d
