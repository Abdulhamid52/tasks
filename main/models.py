from django.db import models
from django.contrib.auth.models import User
from accounts.models import *

# Create your models here.

class Work(models.Model):
    user = models.ForeignKey(User, related_name="user_work", on_delete=models.CASCADE)
    workers = models.ManyToManyField(Workers, verbose_name="workers", blank=True)
    title = models.CharField("work name", max_length=450)
    salary = models.IntegerField("salary", default=0)
    active = models.BooleanField("active", default=True)
    
    def __str__(self):
        return self.title
    