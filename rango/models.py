from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Id = models.IntegerField(unique=True)
    moneyforbitches =  models.IntegerField(default=0)
    def __unicode__(self):
        return self.user.username