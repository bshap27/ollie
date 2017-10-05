from django import forms
from .models import Pet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'primary_breed', 'mix', 'age')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="My first name is")
    last_name = forms.CharField(max_length=30, label="My last name is")
    username = forms.EmailField(max_length=254, label="My email is")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', )