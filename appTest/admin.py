from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import solarHeater

# Register your models here.
@admin.register(solarHeater)
class solarHeaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')

    def photoPreview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150" height="150" style="object-fit:cover"/>')
        return "No image"

    photoPreview.short_description = 'Photo'