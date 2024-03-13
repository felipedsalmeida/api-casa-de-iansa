from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Orixas(models.TextChoices):
    IANSA = "Iansã"
    IEMANJA = "Iemanjá"
    NANA = "Nanã"
    OBALUAE = "Obaluaê"
    OGUM = "Ogum"
    OXAGUIA = "Oxaguiã"
    OXALA = "Oxalá"
    OXALUFA = "Oxalufã"
    OXOSSI = "Oxossi"
    OXUM = "Oxum"
    OXUMARE = "Oxumare"
    XANGO = "Xangô"
class Entidade(models.Model):
    orixas = models.CharField(
        choices=Orixas.choices, default=Orixas.OXALA
    )
    caboclo_de_pena = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    caboclo_boiadeiro = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    preto_velho = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    encantados = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    povo_de_esquerda = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    criancas = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    odu_da_testa = models.CharField()
    odu_da_nuca = models.CharField()
    odu_do_nascimento = models.CharField()
    odu_adjunto = models.CharField()
    odu_negativo = models.CharField()
    odu_positivo = models.CharField()
    