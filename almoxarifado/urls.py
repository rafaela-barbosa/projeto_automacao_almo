from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColaboradorViewSet, AtivoViewSet, MovimentacaoViewSet

router = DefaultRouter()
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'ativos', AtivoViewSet)
router.register(r'movimentacoes', MovimentacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]