from django.shortcuts import render, redirect
from . forms import AppointmentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')

#Register and login
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('diagnosis')  # Redirect to home or any other page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# views.py
@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Diagnosis
def diagnosis(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect to a success page or list of appointments
    else:
        form = AppointmentForm()

    return render(request, 'add_book.html', {'form': form})


from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'confirmation.html', {'appointments': appointments})

from django.contrib.auth.decorators import login_required
from .models import UserProfile
@login_required
def profile(request):
    # Get the user profile for the currently logged-in user
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})