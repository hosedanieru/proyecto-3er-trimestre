from rest_framework import viewsets
from .models import Grano
from .serializers import GranoSerializer

class GranoViewSet(viewsets.ModelViewSet):
    queryset = Grano.objects.all()
    serializer_class = GranoSerializer
