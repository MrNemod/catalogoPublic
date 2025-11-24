from django.contrib import admin
from .models import *

class SolarHeaterImageInline(admin.TabularInline):
    model = productImage
    extra = 1

class solarLightImageInline(admin.TabularInline):
    model = productImage
    extra = 1

class TestProductImageInline(admin.TabularInline):
    model = productImage
    extra = 1

@admin.register(solarHeater)
class SolarHeaterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description',)
    inlines = [SolarHeaterImageInline]

@admin.register(solarLight)
class SolarLightAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description',)
    inlines = [solarLightImageInline]

@admin.register(testProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description',)
    inlines = [TestProductImageInline]