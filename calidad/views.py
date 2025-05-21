from rest_framework import viewsets
from .models import calidad
from .serializers import calidadSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = calidad.objects.all()
    serializer_class = calidadSerializer