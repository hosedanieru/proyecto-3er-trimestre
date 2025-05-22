from django.db import models
from lotes.models import Lote

class EtapaProcesamiento(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    etapa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'{self.etapa} - {self.lote.codigo}'
