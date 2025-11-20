from django.shortcuts import render
from theme import templates

# Create your views here.

def index(request):
    return render(request, 'base.html')

def test(request):
    return render(request, 'base1.html')