from rest_framework import serializers
from hencasa.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['us_nombre','us_apellidos']