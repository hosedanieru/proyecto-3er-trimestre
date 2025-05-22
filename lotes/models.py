from django.db import models

class Lote(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    grano = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # o 'granos.Grano'
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.codigo
