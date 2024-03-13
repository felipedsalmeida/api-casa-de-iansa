from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Medium,Medium_Funcoes
from enderecos.models import Endereco
from enderecos.serializers import EnderecoSerializer
from emergencias.models import Emergencia
from emergencias.serializers import EmergenciaSerializer
from entidades.models import Entidade
from entidades.serializers import EntidadeSerializers
from batizados.models import Batizado
from batizados.serializers import BatizadoSerializers
from camarinhas.models import Camarinha
from camarinhas.serializers import CamarinhaSerializers

class MediumSerializer (serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    
    contato_emergencia = EmergenciaSerializer()

    entidades = EntidadeSerializers()

    camarinha = CamarinhaSerializers()

    batizado = BatizadoSerializers()

    def create(self, validated_data:dict) -> Medium:
        endereco_data = validated_data.pop("endereco")
        endereco = Endereco.objects.create(**endereco_data)

        contato_emergencia_data = validated_data.pop("contato_emergencia")
        contato_emergencia = Emergencia.objects.create(**contato_emergencia_data)

        entidades_data = validated_data.pop("entidades")
        entidades = Entidade.objects.create(**entidades_data)

        camarinha_data = validated_data.pop("camarinha")
        camarinha = Camarinha.objects.create(**camarinha_data)

        batizado_data = validated_data.pop("batizado")
        batizado = Batizado.objects.create(**batizado_data)


        admin = validated_data.get("admin")

        if admin == True:
            medium = Medium.objects.create_superuser(endereco=endereco, contato_emergencia=contato_emergencia, entidades=entidades, batizado=batizado, camarinha=camarinha, **validated_data)
        else:
            medium = Medium.objects.create_user(endereco=endereco, contato_emergencia=contato_emergencia, entidades=entidades, batizado=batizado, camarinha=camarinha, **validated_data)
        
        # for contato_data in contato_emergencia_data:
        #     Emergencia.objects.create(medium=medium, **contato_data)    
        
        return medium

    class Meta:
        model = Medium
        fields = [
            "id",
            "username",
            "password",
            "nome",
            "sobrenome",
            "data_de_nascimento",
            "identidade",
            "cpf",
            "telefone",
            "email",
            "profissao",
            "funcao",
            "observacoes",
            "admin",
            "amaci",
            "endereco",
            "contato_emergencia",
            "entidades",
            "batizado",
            "camarinha",
            "created_at"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "contato_emergencia": {"many": True},
            "created_at": {"read_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Medium.objects.all(),
                        message="Um usuário com este username já existe."
                    )
                ]
            },
            "identidade": {
                "validators": [
                    UniqueValidator(
                        queryset=Medium.objects.all(),
                        message="Um usuário com este email já existe."
                    )
                ]
            },
            "cpf": {
                "validators": [
                    UniqueValidator(
                        queryset=Medium.objects.all(),
                        message="Um usuário com este cpf já existe."
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Medium.objects.all(),
                        message="Um usuário com este email já existe."
                    )
                ]
            }
        }
    # id = serializers.UUIDField(read_only=True)
    # username = serializers.CharField(max_length=150)
    # senha = serializers.CharField(max_length=128, write_only=True)
    # nome = serializers.CharField(max_length=50)
    # sobrenome = serializers.CharField(max_length=50)    
    # data_de_nascimento = serializers.DateTimeField()
    # identidade = serializers.IntegerField()
    # cpf = serializers.IntegerField()
    # profissao = serializers.CharField()
    # funcao = serializers.ChoiceField(
    #     choices=Medium_Funcoes.choices, default=Medium_Funcoes.MEDIUM_DESENVOLVIMENTO
    # )
    # observacoes = serializers.CharField(required=False)
    # admin = serializers.BooleanField(required=False)
    
    