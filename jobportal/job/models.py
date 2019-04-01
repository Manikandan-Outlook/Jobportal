from datetime import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage

class JobUser(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    resume_title = models.CharField(max_length=1000, blank=False, null=False)
    resume=models.FileField(upload_to='resume/', blank=False)
    created_datetime = models.DateTimeField(default=datetime.now())
