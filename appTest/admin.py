from django.contrib import admin
from .models import solarHeater, solarLight, productImage

class SolarHeaterImageInline(admin.TabularInline):
    model = productImage
    extra = 1

class solarLightImageInline(admin.TabularInline):
    model = productImage
    extra = 1

@admin.register(solarHeater)
class SolarHeaterAdmin(admin.ModelAdmin):
    inlines = [SolarHeaterImageInline]

@admin.register(solarLight)
class SolarLightAdmin(admin.ModelAdmin):
    inlines = [solarLightImageInline]