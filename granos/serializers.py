from rest_framework import serializers
from .models import Grano

class GranoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grano
        fields = '__all__'
