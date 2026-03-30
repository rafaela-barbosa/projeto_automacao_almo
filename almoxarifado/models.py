from django.db import models

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    tag_rfid = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="TAG RFID")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
    

class Ativo(models.Model):
    STATUS_CHOICES = [
        ('ESTOQUE', 'Disponível em Estoque'),
        ('USO', 'Em uso / Retirado'),
        ('MANUTENÇÃO', 'Em Manutenção'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Equipamento")
    cod_id = models.CharField(max_length=50, unique=True, verbose_name="Código de Barras / ID") # Este campo será preenchido pelo Scanner de RFID no ESP32
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ESTOQUE')
    descricao = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"{self.nome} - ({self.cod_id})"
    

class Movimentacao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, verbose_name="Equipamento")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True, verbose_name="Responsável")
    data_saida = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True, verbose_name="Data de Devolução")

    def __str__(self):
        status = "Em Uso" if not self.data_devolucao else "Devolvido"
        return f"{self.ativo.nome} -> {self.colaborador.nome} ({status})"
    
    def save(self, *args, **kwargs):
        if not self.data_devolucao:
            self.ativo.status = 'USO'  # Se não tem data de devolução, o item está sendo RETIRADO. muda status para Em uso / Retirado
        else:
            self.ativo.status = 'ESTOQUE'  # Se tem data de devolução, o item está VOLTANDO. muda status para Disponível em Estoque
        
        self.ativo.save()
        super().save(*args, **kwargs)