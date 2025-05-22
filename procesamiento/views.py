from rest_framework import viewsets
from .models import EtapaProcesamiento
from .serializers import EtapaProcesamiento

class LoteViewSet(viewsets.ModelViewSet):
    queryset = EtapaProcesamiento.objects.all()
    serializer_class = EtapaProcesamiento
