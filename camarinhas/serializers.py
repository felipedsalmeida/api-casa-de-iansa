from rest_framework import serializers
from .models import Camarinha
class CamarinhaSerializers(serializers.ModelSerializer):
    def create(self, validated_data:dict) -> Camarinha:
        return Camarinha.objects.create(**validated_data)
    class Meta:
        model = Camarinha
        fields = [
            "data",
            "madrinha",
            "padrinho"
        ]