from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser para
    incluir un campo 'rol' con opciones definidas.
    """
    
    ADMIN = 'admin'
    OPERARIO = 'operario'
    CALIDAD = 'calidad'
    
    ROL_CHOICES = [
        (ADMIN, 'Administrador'),
        (OPERARIO, 'Operario'),
        (CALIDAD, 'Supervisor de Calidad'),
    ]
    
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default=OPERARIO,
        help_text="Rol del usuario en el sistema"
    )
    
    # Campos adicionales opcionales
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
    
    def es_admin(self):
        return self.rol == self.ADMIN
    
    def es_operario(self):
        return self.rol == self.OPERARIO
    
    def es_calidad(self):
        return self.rol == self.CALIDAD
