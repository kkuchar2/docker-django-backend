import os


def envv(name, default=None):
    return os.environ.get(name, default)


def check_envv_exists_and_get(name):
    v = envv(name)
    if v is None:
        print("{} is not set!".format(name))
    return v
