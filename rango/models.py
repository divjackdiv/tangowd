from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    balance =  models.FloatField(default=0)

class EMessage(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(null = False)
