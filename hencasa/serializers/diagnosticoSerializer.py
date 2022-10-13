from rest_framework import serializers
from hencasa.models.diagnostico import Diagnostico

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diagnostico
        fields='__all__'