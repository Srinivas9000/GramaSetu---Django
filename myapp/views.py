from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def panchaiyeti(request):
    return render(request, "panchaiyeti.html")


def temples(request):
    return render(request, "temples.html")


def tourism(request):
    return render(request, "tourism.html")

def farming(request):
    return render(request, "farming.html")

def school(request):
    return render(request, "school.html")

def sports(request):
    return render(request, "sports.html")

def services(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your feedback has been submitted.")
            return redirect('services')
    else:
        form = FeedbackForm()

    return render(request, 'services.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Registration successful")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'home.html')
