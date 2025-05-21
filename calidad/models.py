from django.db import models
from lotes.models import Lote

class PruebaCalidad(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    impurezas = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=100)
    fecha_prueba = models.DateField()

    def __str__(self):
        return f'Prueba de calidad - {self.lote.codigo}'
