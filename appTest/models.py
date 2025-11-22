from django.db import models
from .storage_backend import ImageKitStorage

# Create your models here.

class solarHeater(models.Model):
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
    name = models.CharField(max_length=100,null=False, blank=False, verbose_name="Nombre")
    description = models.TextField( blank=False, null=False, verbose_name="Descripcion")
    price = models.IntegerField( blank=False, null=False, verbose_name="Precio")
    liters = models.IntegerField( blank=False, null=False, verbose_name="Litros")
    persons = models.IntegerField( blank=False, null=False, verbose_name="Personas")
    number_of_tubes = models.IntegerField( blank=False, null=False, verbose_name="Numero de tubos")
    brand = models.CharField(max_length=100, blank=False, null=False,  verbose_name="Marca")

    def __str__(self):
        return self.name

class solarHeaterImage(models.Model):
    heater = models.ForeignKey(
        solarHeater,
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(storage=ImageKitStorage, blank=False, null=False,  verbose_name="Imagen(es)")
    def __str__(self):
        return f'Imagen de {self.heater.name}'