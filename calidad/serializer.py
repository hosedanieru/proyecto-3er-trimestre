from rest_framework import serializers
from .models import PruebaCalidad

class PruebaCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaCalidad
        fields = '__all__'
