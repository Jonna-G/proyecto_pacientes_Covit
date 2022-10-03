from rest_framework import serializers
from hencasa.models.asignacion import Asignacion

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asignacion
        fields='__all__'