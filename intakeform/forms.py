from django import forms
from .models import Pet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ('name', 'email',)

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'primary_breed', 'mix', 'age')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required.')
    last_name = forms.CharField(max_length=30, help_text='Required.')
    username = forms.EmailField(max_length=254, help_text='Required.', label="Email")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', )