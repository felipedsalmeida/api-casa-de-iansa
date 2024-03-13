from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField()
    numero = models.CharField()
    cep = models.IntegerField()
    cidade = models.CharField()
    estado = models.CharField(max_length=2)