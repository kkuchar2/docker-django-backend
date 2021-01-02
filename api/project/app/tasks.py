from celery_kuchkr.mycelery import celery_app


@celery_app.task
def dummy_task(a, b):
    print("Dummy periodic task: (a: {}, b: {})".format(a, b))


dummy_task(0, 0)
