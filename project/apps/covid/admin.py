from django.contrib import admin

from .models import CovidStats, CovidCalcs

admin.site.register(CovidStats)

admin.site.register(CovidCalcs)
