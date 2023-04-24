from django.shortcuts import render
from django.http import request
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    
    data = {
        "teams": team,
        "featured_cars":featured_cars,
        "all_cars":all_cars,
        "model_search":model_search,
        "city_search": city_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
        }   
    return render(request, 'pages/home.html', data)

def about(request):
    team =  Team.objects.all()
   
    data = {
        "teams": team
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')


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