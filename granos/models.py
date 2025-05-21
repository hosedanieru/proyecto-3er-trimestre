from django.db import models

class Grano(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
