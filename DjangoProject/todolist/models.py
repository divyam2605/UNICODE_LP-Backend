from asyncio.windows_events import NULL
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    completion_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

