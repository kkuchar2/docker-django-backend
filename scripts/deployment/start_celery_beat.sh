#!/usr/bin/env bash

cd project
celery -A celery_kuchkr beat -l debug