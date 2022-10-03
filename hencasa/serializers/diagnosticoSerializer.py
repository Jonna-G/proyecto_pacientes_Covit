from rest_framework import serializers
from hencasa.models.diagnostico import Diagnostico

class DiagnosticoSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Diagnostico
        fields='__all__'