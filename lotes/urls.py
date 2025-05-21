from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoteViewSet

router = DefaultRouter()
router.register(r'Lotes', LoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]