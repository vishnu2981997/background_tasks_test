from django.db import models


# Create your models here.
class ImportRequest(models.Model):
    owner = models.ForeignKey('auth.User', related_name='import_requests', on_delete=models.CASCADE)
    url = models.CharField(max_length=1024, unique=False, blank=False)
    access_token = models.CharField(max_length=1024, unique=False, blank=False)
    queue_url = models.CharField(max_length=1024, unique=False, blank=False)
    running = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    started = models.DateTimeField(editable=False)
    ended = models.DateTimeField(editable=False)

    class Meta:
        ordering = ('url',)

    def __str__(self):
        return self.url
