from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

# Create your models here.

class Workers(models.Model):
    name = models.CharField("name", max_length=150)
    surname = models.CharField("surname", max_length=150)
    works = models.IntegerField("all works", default=0)
    money = models.IntegerField("money", default=0)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_pro", on_delete=models.CASCADE)
    name = models.CharField("name", max_length=150)
    surname = models.CharField("surname", max_length=150)
    workers = models.ManyToManyField(Workers, verbose_name="workers", blank=True)

    def __str__(self):
        return self.name
    
