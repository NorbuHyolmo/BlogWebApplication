from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1000, default= "null")
    wake_up = models.TimeField()
    coding_hours_start = models.TimeField(default=timezone.now)
    coding_hours_end = models.TimeField(default=timezone.now)
    exercise = models.CharField(max_length=100)
    remarks = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
