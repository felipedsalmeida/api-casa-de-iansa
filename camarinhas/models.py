from django.db import models

# Create your models here.
class Camarinha(models.Model):
    data = models.DateTimeField()
    madrinha = models.CharField()
    padrinho = models.CharField()
