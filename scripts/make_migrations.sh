#!/usr/bin/env bash

docker-compose run klkuch_server python manage.py makemigrations accounts -v 3
docker-compose run klkuch_server python manage.py makemigrations api -v 3
