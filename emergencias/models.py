from django.db import models

# Create your models here.
class Emergencia(models.Model):
    nome = models.CharField()
    telefone = models.BigIntegerField()
    parentesco = models.CharField()
    # medium = models.ForeignKey("mediuns.Medium", on_delete=models.CASCADE)