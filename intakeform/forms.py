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

class IntakeForm(forms.Form):
    name = forms.CharField(max_length=30, label="My name is", label_suffix='')
    pups_name = forms.CharField(max_length=30, label="and my pup\'s name is", label_suffix='')
    email = forms.EmailField(max_length=254, label="My email is", label_suffix='')
    breed_type = forms.ChoiceField(choices=(('', ''),('single','single breed'), ('double','combo of two breeds'), ('mix','mix')), label="", label_suffix='')
    breed_1 = forms.CharField(max_length=30, label='of a', label_suffix='', required=False)
    breed_2 = forms.CharField(max_length=30, label='and a', label_suffix='', required=False)
    sex = forms.ChoiceField(choices=[('',''),('M','He'), ('F','She')], label="", label_suffix='')
    fixed = forms.ChoiceField(choices=[('N','not neutered'),('Y', 'neutered')], label="and is", label_suffix='')
    # birth_month = forms.ChoiceField(choices=[('',''),('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], label="", label_suffix='')
    # birth_year = forms.IntegerField(label=',', label_suffix='', max_value=2017)
    birth = forms.DateField(label='', label_suffix='', input_formats=['%m/%Y'], widget=forms.TextInput(attrs={'placeholder': 'MM/YYYY'}))
    active = forms.ChoiceField(choices=[('',''),('lazy','a bit lazy'), ('active','pretty active'), ('hyper','hyper')], label='', label_suffix='')
    weight = forms.IntegerField(label='', label_suffix='', help_text="pounds", min_value=1)
    build = forms.ChoiceField(choices=[('',''),('skinny','skinny'), ('ideal','ideal'), ('chubby','chubby')], label='', label_suffix='')
    allergies = forms.CharField(max_length=200, label='', label_suffix='', initial="nothing")