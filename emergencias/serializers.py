from rest_framework import serializers
from emergencias.models import Emergencia

class EmergenciaSerializer(serializers.ModelSerializer):
    def create(self, validated_data:list) -> Emergencia:
        return Emergencia.objects.create(**validated_data)
    class Meta:
        model = Emergencia
        fields = [
            "id",
            "nome",
            "telefone",
            "parentesco"
        ]