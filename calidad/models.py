from django.db import models
from .models import Calidad

class Calidad(models.Model):
    codigo = models.CharField(max_length=100)
    # otros campos...

    def __str__(self):
        return self.codigo

class PruebaCalidad(models.Model):
    lote = models.ForeignKey(Calidad, on_delete=models.CASCADE)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    impurezas = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=100)
    fecha_prueba = models.DateField()

    def __str__(self):
        return f'Prueba de calidad - {self.lote.codigo}'
