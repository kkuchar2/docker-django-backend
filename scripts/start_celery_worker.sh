#!/usr/bin/env bash

cd project
celery -A celery worker -l debug --uid=nobody --gid=nogroup