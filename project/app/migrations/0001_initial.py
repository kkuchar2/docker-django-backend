# Generated by Django 3.1.3 on 2020-12-22 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COVID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, null=True, unique=True)),
                ('count', models.IntegerField(default=0, null=True)),
                ('cases_cumulative', models.IntegerField(default=0, null=True)),
                ('deaths', models.IntegerField(default=0, null=True)),
                ('deaths_cumulative', models.IntegerField(default=0, null=True)),
                ('recoveries', models.IntegerField(default=0, null=True)),
                ('recoveries_cumulative', models.IntegerField(default=0, null=True)),
                ('active_cases', models.IntegerField(default=0, null=True)),
                ('hospitalized', models.IntegerField(default=0, null=True)),
                ('on_quarantine', models.IntegerField(default=0, null=True)),
                ('on_supervision', models.IntegerField(default=0, null=True)),
                ('used_beds', models.IntegerField(default=0, null=True)),
                ('respirators', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
