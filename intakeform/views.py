import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .forms import PetForm, SignUpForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    bkgdcolor = "peach"
    # return render(request, 'intakeform/index.html', {})
    return render_to_response('intakeform/index.html', locals())
# OR....
# def my_view(request):
#     posts = BlogPosts.objects.all()
#     return render(request, 'posts.html', locals())


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('pet_new')
    else:
        form = SignUpForm()
    return render(request, 'intakeform/signup.html', {'form': form})

@login_required
def pet_new(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.created_date = timezone.now()
            pet.user_id = request.user
            pet.save()
            return redirect('index')
    else:
        form = PetForm()
    return render(request, 'intakeform/pet_edit.html', {'form': form})