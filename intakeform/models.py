import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
# from django.contrib.auth.validators import ASCIIUsernameValidator


class Pet(models.Model):
    # user = models.ForeignKey('auth.User')
    userprofile = models.ForeignKey('UserProfile')
    name = models.CharField(max_length=200)
    mix = models.BooleanField()
    breed1 = models.CharField(max_length=200, blank=True, null=True)
    breed2 = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=3)
    fixed = models.BooleanField()
    birth = models.CharField(max_length=200)
    active = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    build = models.CharField(max_length=200)
    allergies = models.CharField(max_length=200, blank=True, null=True)
    eats = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def breed_mix(self):
        if self.mix == True:
            return 'mix'
        elif not bool(self.breed2): # breed2 is empty
            return self.breed1
        else:
            return self.breed1 + ' and ' + self.breed2 + ' mix'

# http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/
class UserProfile(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_date = models.DateTimeField()
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    #     blank=True,
    #     null=True
    # )
    # def create(cls, title):
    #     book = cls(title=title)
    #     # do something with the book
    #     return book