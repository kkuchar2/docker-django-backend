#!/usr/bin/env bash

cd project
celery -A worker beat -l debug --uid=nobody --gid=nogroup