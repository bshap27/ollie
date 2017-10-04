import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PetForm #, UserForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# def login_user(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         # ...
#     else:
#         # Return an 'invalid login' error message.
#         # ...

def index(request):
    return render(request, 'intakeform/index.html', {})
    # return HttpResponse("Hello, world. You're at the intake form index.")

# def user_new(request):
#     form = UserForm()
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.created_date = timezone.now()
#             user.save()
#             return redirect('pet_new')
#     else:
#         form = UserForm()
#     return render(request, 'intakeform/user_edit.html', {'form': form})

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