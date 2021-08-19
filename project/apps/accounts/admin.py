from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from .models import UserProfile

admin.site.unregister(Site)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'domain', 'name')
    search_fields = ('domain', 'name')
    ordering = ['id']


UserModel = get_user_model()


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfile)