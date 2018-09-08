from django.db import models
from django.conf import settings

# Create your models here.

class ToDo(models.Model):
    message = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    def __str__(self):
        return '{}''{}'.format(self.datetime,self.message)