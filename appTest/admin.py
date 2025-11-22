from django.contrib import admin
from .models import solarHeater, solarHeaterImage

class SolarHeaterImageInline(admin.TabularInline):
    model = solarHeaterImage
    extra = 1

@admin.register(solarHeater)
class SolarHeaterAdmin(admin.ModelAdmin):
    inlines = [SolarHeaterImageInline]