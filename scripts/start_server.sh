#!/usr/bin/env bash

cd project

python manage.py makemigrations --no-input
python manage.py makemigrations site --no-input
python manage.py makemigrations celery_kuchkr
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createmasteruser
python manage.py runserver 0.0.0.0:5000