import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# from django.contrib.auth.models import User
# from django.contrib.auth.validators import ASCIIUsernameValidator

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     created_date = models.DateTimeField()

#     def __str__(self):
#         return self.name

class Pet(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    primary_breed = models.CharField(max_length=200)
    mix = models.BooleanField()
    age = models.IntegerField(default=0)
    created_date = models.DateTimeField()
    # user_id = models.ForeignKey(User)

    def __str__(self):
        return self.name
