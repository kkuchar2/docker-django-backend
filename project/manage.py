#!/usr/bin/env python

import os
import sys
import time

from django.core.management import execute_from_command_line
from django.db.utils import OperationalError
from django.db import connection


def exec_command(args):
    execute_from_command_line(["manage_py", *args])


if __name__ == '__main__':
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings.settings"

    db_conn = None

    print("Waiting for database...")

    while not db_conn:
        try:
            connection.ensure_connection()
            db_conn = True
        except OperationalError:
            print('Database unavailable, waiting 1 second...')
            time.sleep(1)

    print("Database available")

    exec_command(["migrate"])
    exec_command(["updatedefaultsite"])
    exec_command(["collectstatic", "--no-input"])
    exec_command(["createmasteruser"])
    exec_command(["runserver", "0.0.0.0:8000"])
