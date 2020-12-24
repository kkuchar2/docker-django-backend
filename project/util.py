import os


def envv(name, default=None):
    return os.environ.get(name, default)
