from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'type', 'enabled', 'comment', )
    list_filter = ('type', 'enabled')
