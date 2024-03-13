from rest_framework import serializers
from entidades.models import Entidade, Orixas

class EntidadeSerializers(serializers.ModelSerializer):
    def create(self, validated_data:dict) -> Entidade:
        return Entidade.objects.create(**validated_data)
    class Meta:
        model = Entidade
        fields = [
            "orixas",
            "caboclo_de_pena",
            "caboclo_boiadeiro",
            "preto_velho",
            "encantados",
            "povo_de_esquerda",
            "criancas",
            "odu_da_testa",
            "odu_da_nuca",
            "odu_do_nascimento",
            "odu_adjunto",
            "odu_negativo",
            "odu_positivo"
        ]
        # extra_kwargs = {
        #     "povo_de_esquerda": {"many": True},
        #     "caboclo_de_pena": {"many": True},
        #     "caboclo_boiadeiro": {"many": True},
        #     "preto_velho": {"many": True},
        #     "encantados": {"many": True},
        #     "criancas": {"many": True},
        # }