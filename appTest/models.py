from django.db import models
from .storage_backend import ImageKitStorage

# Create your models here.

class base_model(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    description = models.TextField(blank=False, null=False, verbose_name="Descripcion")
    price = models.IntegerField(blank=False, null=False, verbose_name="Precio")
    brand = models.CharField(max_length=100, blank=False, null=False, verbose_name="Marca")

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

class solarHeater(base_model):
    liters = models.IntegerField( blank=False, null=False, verbose_name="Litros")
    persons = models.IntegerField( blank=False, null=False, verbose_name="Personas")
    number_of_tubes = models.IntegerField( blank=False, null=False, verbose_name="Numero de tubos")

    class Meta:
        verbose_name_plural = 'Calentadores'
        verbose_name = 'Calentador'

    def __str__(self):
        return self.name

class solarLight(base_model):
    watts = models.IntegerField( blank=False, null=False, verbose_name="Watts")
    duration = models.IntegerField( blank=False, null=False, verbose_name="Duracion")
    class Meta:
        verbose_name_plural = 'Lamparas solares'
        verbose_name = 'Lampara solar'

class testProduct(base_model):
    test = models.IntegerField( blank=False, null=False, verbose_name="Test")
    test2 = models.EmailField(blank=False, null=False, verbose_name="Email")
    test3 = models.DateField(blank=False, null=False, verbose_name="Date")

# Agregar productos antes de esta linea
class productImage(models.Model):
    product = models.ForeignKey(
        base_model,
        related_name='images',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    image = models.ImageField(
        storage=ImageKitStorage,
        blank=False,
        null=False,
        verbose_name="Imagen"
    )

    def __str__(self):
        return f'Imagen de {self.product.name}'