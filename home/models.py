from django.db import models
from django.contrib.auth.models import User

from asgiref.sync import async_to_sync

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        super(Notification, self).save(*args, **kwargs)