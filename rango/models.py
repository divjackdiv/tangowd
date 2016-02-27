from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
<<<<<<< HEAD
    balance =  models.FloatField(default=0)

class EMessage(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(null = False)
=======
    userfn = models.CharField(max_length=20)
    userln = models.CharField(max_length=20)
    balance =  models.IntegerField(default=0)



>>>>>>> eb71a171e7603838f9a32f4513a662b7e0da5efc
