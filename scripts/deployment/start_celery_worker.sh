#!/usr/bin/env bash

cd project
celery --app=celery_kuchkr worker \
       --loglevel=INFO \
       --uid=nobody --gid=nogroup