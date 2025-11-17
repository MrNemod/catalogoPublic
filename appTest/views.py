from django.shortcuts import render
import theme

# Create your views here.

def index(request):
    return render(request, 'base1.html')

def home(request):
    return render(request, 'base.html')