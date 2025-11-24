from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *

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
    lights = solarLight.objects.prefetch_related('images').all()
    tests = testProduct.objects.prefetch_related('images').all()
    all_data = []
    for heater in heaters:
        first_image = heater.images.first()
        all_data.append({
            'id': heater.id,
            'name': heater.name,
            'description': heater.description,
            'price': heater.price,
            'liters': heater.liters,
            'persons': heater.persons,
            'number_of_tubes': heater.number_of_tubes,
            'brand': heater.brand,
            'image': first_image.image if first_image.image else None,
        })

    for light in lights:
        first_image = light.images.first()
        all_data.append({
            'id': light.id,
            'name': light.name,
            'description': light.description,
            'price': light.price,
            'brand': light.brand,
            'watts': light.watts,
            'duration': light.duration,
            'image': first_image.image if first_image.image else None,
        })

    for test in tests:
        first_image = test.images.first()
        all_data.append({
            'id': test.id,
            'name': test.name,
            'description': test.description,
            'price': test.price,
            'brand': test.brand,
            'test': test.test,
            'test2': test.test2,
            'test3': test.test3,
            'image': first_image.image if first_image.image else None,
        })

    return render(request, 'index.html', {"products": all_data})

# Vista dinamica de los productos
EXCLUDED_FIELDS = ['id', 'description', 'price', 'brand', 'product', 'base_model_ptr']
def details(request, product_id):
    # Para agregar nuevas categorias solo seguir la misma estructura
    try:
        product = solarHeater.objects.get(pk=product_id)
    except solarHeater.DoesNotExist:
        try:
            product = solarLight.objects.get(pk=product_id)
        except solarLight.DoesNotExist:
            try:
                product = testProduct.objects.get(pk=product_id)
            except testProduct.DoesNotExist:
                raise Http404("El producto no existe.")

    # No hace falta cambiar nada aqui abajo
    dynamic_specs = []

    for field in product._meta.fields:
        field_name = field.name

        if field_name not in EXCLUDED_FIELDS:
            label = field.verbose_name
            value = getattr(product, field_name)

            if field_name == 'liters':
                value = f"{value} L"
            elif field_name == 'watts':
                value = f"{value} W"

            dynamic_specs.append({
                'label': label,
                'value': value,
            })

    context = {
        'product': product,
        'dynamic_specs': dynamic_specs,
    }

    return render(request, 'product.html', context)
