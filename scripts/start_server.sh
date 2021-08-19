#!/usr/bin/env bash

cd project || exit

python manage.py makemigrations --no-input
python manage.py makemigrations main --no-input
python manage.py makemigrations accounts --no-input
python manage.py makemigrations covid --no-input
python manage.py migrate --noinput
python manage.py collectstatic --noinput -v 0
python manage.py createmasteruser

#if [ "$PRODUCTION_ENV" == "True" ]; then
#  cd ..
#  gunicorn -k uvicorn.workers.UvicornWorker project.asgi:application --bind 0.0.0.0:8000 --workers 3
#else
python manage.py runserver 0.0.0.0:5000
#fi
