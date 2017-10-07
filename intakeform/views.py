import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .forms import SignUpForm, IntakeForm #, PetForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Pet, UserProfile
import pdb # debugger
# pdb.set_trace()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'intakeform/signup.html', {'form': form})

def intake_form(request):
    if request.method=='POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            prof = UserProfile(full_name=cd.get('full_name'), email=cd.get('email'))
            if not UserProfile.objects.filter(email = cd.get('email')).exists():
                prof.created_date = timezone.now()
                prof.save()
            else:
                prof = UserProfile.objects.get(email = cd.get('email'))

            pet = Pet(
                name = cd.get('pups_name'),
                mix = True if cd.get('breed_type') == 'mix' else False,
                breed1 = cd.get('breed1'),
                breed2 = cd.get('breed2'),
                sex = cd.get('sex'),
                fixed = cd.get('fixed'),
                birth = cd.get('birth'),
                active = cd.get('active'),
                weight = cd.get('weight'),
                build = cd.get('build'),
                allergies = cd.get('allergies'),
                created_date = timezone.now(),
                userprofile = prof
                )
            pet.save()

            return render(request, 'intakeform/intake_summary.html', {'pet': pet, 'bkgdcolor': "peach"})
        else:
            request.session['form_data'] = request.POST
            return redirect('/')
    else:
        form_data = request.session.get('form_data', None)
        form = IntakeForm(form_data)
    return render(request, 'intakeform/intake_form.html', {'form': form})


# @login_required
# def pet_new(request):
#     form = PetForm()
#     if request.method == "POST":
#         form = PetForm(request.POST)
#         if form.is_valid():
#             pet = form.save(commit=False)
#             pet.created_date = timezone.now()
#             pet.user_id = request.user
#             pet.save()
#             return redirect('index')
#     else:
#         form = PetForm()
#     return render(request, 'intakeform/pet_edit.html', {'form': form})