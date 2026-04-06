from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Colaborador, Ativo, Movimentacao
from .serializers import ColaboradorSerializer, AtivoSerializer, MovimentacaoSerializer

# Create your views here.
class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cod_id']

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer