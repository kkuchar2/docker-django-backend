#!/usr/bin/env bash

cd klkuch_server_code

./wait-for-it.sh -q db:3307 -- python manage.py makemigrations \
&& python manage.py migrate \
&& python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin@example.com').delete(); User.objects.create_superuser('admin@example.com', 'admin', 'admin')" \
&& python manage.py runserver 0.0.0.0:5000 && python manage.py collectstatic
