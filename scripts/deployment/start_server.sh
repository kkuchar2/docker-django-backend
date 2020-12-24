#!/usr/bin/env bash

echo "cd project"
cd project

echo "python manage.py makemigrations --no-input"
python manage.py makemigrations --no-input

echo "python manage.py makemigrations app --no-input"
python manage.py makemigrations app --no-input

echo "python manage.py makemigrations celery_kuchkr"
python manage.py makemigrations celery_kuchkr

echo "manage.py migrate --noinput"
python manage.py migrate --noinput

echo "manage.py collectstatic --noinput  --clear"
python manage.py collectstatic --noinput  --clear

echo "Creating adminitrator account"
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin@example.com').delete(); User.objects.create_superuser('admin@example.com', 'admin', 'admin')" \

echo "Starting server"
python manage.py runserver 0.0.0.0:5000
