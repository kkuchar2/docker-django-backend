import datetime

from django.db import models


class COVID(models.Model):
    date = models.DateField(null=True, default=datetime.date.today)
    count = models.IntegerField(null=True, default=0)
