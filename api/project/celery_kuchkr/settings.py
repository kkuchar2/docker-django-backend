from celery.schedules import timedelta

from util import envv

SECRET_KEY = envv('SECRET_KEY')

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_BEAT_SCHEDULE = {
    "runs-every-1-hour": {
        "task": "app.tasks.dummy_task",
        "schedule": timedelta(hours=1),
        "args": (16, 16)
    }
}
