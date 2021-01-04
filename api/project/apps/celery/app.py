from celery import Celery

import apps.celery.celeryconfig as celeryconfig

app = Celery('apps.celery')
app.config_from_object(celeryconfig)
app.autodiscover_tasks()
