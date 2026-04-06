from rest_framework import serializers
from .models import Colaborador, Ativo, Movimentacao

# transforma modelos em dados que o ESP32 entende. JSON

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = '__all__'

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = '__all__'