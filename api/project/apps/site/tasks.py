from apps.celery import celery as app


@app.task
def dummy_task():
    print("Dummy periodic task")
