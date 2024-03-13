
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Medium_Funcoes(models.TextChoices):

    PAI_DE_SANTO = "Pai de Santo"
    MAE_DE_SANTO = "Mãe de Santo"
    PAI_PEQUENO = "Pai Pequeno"
    MAE_PEQUENA = "Mãe Pequena"
    IAO = "Iaô"
    OGAN = "Ogã"
    MEDIUM_DE_TRABALHO = "Médium de Trabalho"
    MEDIUM_DESENVOLVIMENTO = "Médium em Desenvolvimento"

class Medium(AbstractUser):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)    
    data_de_nascimento = models.DateTimeField()
    identidade = models.IntegerField(unique=True)
    cpf = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    profissao = models.CharField()
    funcao = models.CharField(
        choices=Medium_Funcoes.choices, default=Medium_Funcoes.MEDIUM_DESENVOLVIMENTO
    )
    observacoes = models.TextField(blank=True, null=True)
    admin = models.BooleanField(default=False, blank=True, null=True)
    amaci = models.BooleanField(default=False, blank=True, null=True)
    endereco = models.OneToOneField("enderecos.Endereco", on_delete=models.PROTECT)
    contato_emergencia = models.ForeignKey("emergencias.Emergencia", on_delete=models.PROTECT)
    entidades = models.OneToOneField("entidades.Entidade", on_delete=models.PROTECT)
    batizado = models.OneToOneField("batizados.Batizado", on_delete=models.PROTECT)
    camarinha = models.OneToOneField("camarinhas.Camarinha", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)