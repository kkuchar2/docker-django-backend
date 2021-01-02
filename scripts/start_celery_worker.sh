#!/usr/bin/env bash

cd project
celery -A celery_kuchkr worker -l debug --uid=nobody --gid=nogroup