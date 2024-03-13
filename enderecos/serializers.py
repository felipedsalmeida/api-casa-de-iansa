from rest_framework import serializers

from enderecos.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    def create(self, validated_data:dict) -> Endereco:
        return Endereco.objects.create(**validated_data)
    class Meta:
        model = Endereco
        fields = [
            "id",
            "rua",
            "numero",
            "cep",
            "estado"
        ]