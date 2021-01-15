#!/usr/bin/env bash

cd project

python manage.py makemigrations --no-input
python manage.py makemigrations main --no-input
python manage.py makemigrations accounts --no-input
python manage.py makemigrations covid --no-input
python manage.py makemigrations celery --no-input
python manage.py migrate --noinput
python manage.py collectstatic --noinput -v 0
python manage.py createmasteruser
python manage.py runserver 0.0.0.0:5000
