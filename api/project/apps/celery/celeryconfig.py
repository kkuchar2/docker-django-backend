from celery.schedules import timedelta

from util import envv

SECRET_KEY = envv('SECRET_KEY')

broker_url = 'redis://redis:6379'
result_backend = 'redis://redis:6379'
accept_content = ['application/json']
event_serializer = 'json'
task_serializer = 'json'
timezone = 'UTC'
beat_schedule = {
    "runs-every-1-hour": {
        "task": "site.tasks.dummy_task",
        "schedule": timedelta(hours=1),
        "args": (16, 16)
    }
}
