from django.db import models

# Create your models here.

class solarHeater(models.Model):
    photo = models.ImageField(null = True, upload_to="solar_heaters")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    liters = models.IntegerField()
    persons = models.IntegerField()
    number_of_tubes = models.IntegerField()
    brand = models.CharField(max_length=100)