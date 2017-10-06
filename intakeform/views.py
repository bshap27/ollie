import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .forms import SignUpForm, IntakeForm #, PetForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# import pdb # debugger
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
            pups_name = cd.get('pups_name')
            weight = cd.get('weight')
            breed_type = cd.get('breed_type')
            breed1 = cd.get('breed_1')
            breed2 = cd.get('breed_2')

            if breed_type == 'mix':
                breed = 'mix'
            elif breed_type == 'single':
                breed = breed1
            elif breed_type == 'double':
                breed = breed1 + ' and ' + breed2 + ' mix'
            return render(request, 'intakeform/intake_summary.html', {'breed': breed, 'pups_name': pups_name, 'weight': weight, 'bkgdcolor': "peach"})
    else:
        form = IntakeForm()
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