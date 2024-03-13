from django.db import models

# Create your models here.
class Batizado(models.Model):
    data = models.DateTimeField()
    madrinha = models.CharField()
    padrinho = models.CharField()