#!/usr/bin/env bash

cd project
celery -A celery beat -l info