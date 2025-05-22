from rest_framework import serializers
from .models import login

class GranoSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'
