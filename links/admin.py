from django.contrib import admin

# Register your models here.
from links.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'user', 'is_active', 'num_clicks']
