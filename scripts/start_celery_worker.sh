#!/usr/bin/env bash

cd project
celery -A apps.celery worker -l info --uid=nobody --gid=nogroup