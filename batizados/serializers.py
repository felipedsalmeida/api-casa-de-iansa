from rest_framework import serializers
from .models import Batizado
class BatizadoSerializers(serializers.ModelSerializer):
    def create(self, validated_data:dict) -> Batizado:
        return Batizado.objects.create(**validated_data)
    class Meta:
        model = Batizado
        fields = [
            "data",
            "madrinha",
            "padrinho"
        ]