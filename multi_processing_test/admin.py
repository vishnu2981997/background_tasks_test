from django.contrib import admin
from .models import *


# Register your models here.


class ImportRequestAdmin(admin.ModelAdmin):
    """
    url = models.CharField(max_length=1024, unique=False, blank=False)
    access_token = models.CharField(max_length=1024, unique=False, blank=False)
    queue_url = models.CharField(max_length=1024, unique=False, blank=False)
    running = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    started = models.DateTimeField(null=True, editable=False)
    ended = models.DateTimeField(null=True, editable=False)
    """
    list_display = ("url", "access_token", "queue_url", "running", "created", "started", "ended")
    list_filter = ["url", "access_token", "queue_url", "running", "created", "started", "ended"]
    search_fields = ["url", "access_token", "queue_url", "running"]


admin.site.register(ImportRequest, ImportRequestAdmin)
