from django.shortcuts import render
from .models import solarHeater

# Create your views here.

def base(request):
    filters = solarHeater.objects.all()
    filters_data = []
    for filter in filters:
        filters_data.append({
            'price': filter.price,
            'liters': filter.liters,
            'persons': filter.persons,
            'number_of_tubes': filter.number_of_tubes,
            'brand': filter.brand,
        })
    return render(request, 'base.html', {'filters': filters_data})

def index(request):
    heaters = solarHeater.objects.prefetch_related('images').all()
    heater_data = []
    for heater in heaters:
        first_image = heater.images.first()
        heater_data.append({
            'name': heater.name,
            'description': heater.description,
            'price': heater.price,
            'liters': heater.liters,
            'persons': heater.persons,
            'number_of_tubes': heater.number_of_tubes,
            'brand': heater.brand,
            'image': first_image.image if first_image.image else None,
        })
    return render(request, 'index.html', {"heaters": heater_data, "rango": range(len(heater_data))})
