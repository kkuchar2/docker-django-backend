#!/usr/bin/env bash

docker-compose run klkuch_server python manage.py collectstatic
