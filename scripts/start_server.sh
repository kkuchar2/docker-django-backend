#!/usr/bin/env bash

cd project || exit


python manage.py

#if [ "$PRODUCTION_ENV" == "True" ]; then
#  cd ..
#  gunicorn -k uvicorn.workers.UvicornWorker project.asgi:application --bind 0.0.0.0:8000 --workers 3
#else
#python manage.py runserver 0.0.0.0:8000
#fi
