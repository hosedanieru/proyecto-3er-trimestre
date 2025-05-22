from rest_framework import serializers
from .models import EtapaProcesamiento

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaProcesamiento
        fields = '__all__'
