from django.shortcuts import render
from django.http import request
from .models import Team

# Create your views here.
def home(request):
    team = Team.objects.all()
    data = {
        "teams": team
    }
    return render(request, 'pages/home.html', data)

def about(request):
    team = Team.objects.all()
    data = {
        "teams": team
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'pages/cars.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def services(request):
    return render(request, 'pages/services.html')

def car_details(request):
    return render(request, 'pages/car-details.html')


def search(request):
    return render(request, 'pages/search.html')