from apps.celery import celery_app as app


@app.task
def dummy_task():
    print("Dummy periodic task")
