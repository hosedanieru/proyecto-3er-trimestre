from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalidadViewSet

router = DefaultRouter()
router.register(r'calidad', CalidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
