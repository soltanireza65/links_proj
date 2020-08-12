from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'is_pro', 'user', ]


admin.site.unregister(Group)
