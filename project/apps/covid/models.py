import datetime

from django.db import models


def simple_integer_field(default_value):
    return models.IntegerField(null=True, blank=True, default=default_value)


def simple_decimal_field(default_value):
    return models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6, default=default_value)


class CovidStats(models.Model):
    date = models.DateField(null=True, blank=False, unique=True, default=datetime.date.today)
    cases_daily = simple_integer_field(0)
    cases_cumulative = simple_integer_field(0)
    deaths_daily = simple_integer_field(0)
    deaths_cumulative = simple_integer_field(0)
    recoveries_daily = simple_integer_field(0)
    recoveries_cumulative = simple_integer_field(0)
    active_cases = simple_integer_field(0)
    hospitalized = simple_integer_field(0)
    on_quarantine = simple_integer_field(0)
    on_supervision = simple_integer_field(0)
    used_beds = simple_integer_field(0)
    respirators = simple_integer_field(0)


class CovidCalcs(models.Model):
    cases_daily_increase = simple_decimal_field(0.000000)
    cases_cumulative_increase = simple_decimal_field(0.000000)
    deaths_daily_increase = simple_decimal_field(0.000000)
    deaths_cumulative_increase = simple_decimal_field(0.000000)