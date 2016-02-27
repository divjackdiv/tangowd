from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    userfn = models.CharField(max_length=20)
    userln = models.CharField(max_length=20)
    balance =  models.IntegerField(default=0)








