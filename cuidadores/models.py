from django.db import models
from django.utils import timezone

class Cuidador(models.Model):
    STATUS_CHOICES = [
        ('NOVO', 'Novo Cadastro'),
        ('ENTREVISTA', 'Em Entrevista'),
        ('APROVADO', 'Aprovado'),
        ('REPROVADO', 'Reprovado'),
        ('BLACKLIST', 'LISTA NEGRA - BLOQUEADO'),
    ]

    nome = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    formacao = models.CharField(max_length=100, null=True, blank=True)
    capacitacoes = models.TextField(null=True, blank=True)
    curriculo = models.FileField(upload_to='curriculos/', null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOVO')
    lista_negra = models.BooleanField(default=False)
    
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome