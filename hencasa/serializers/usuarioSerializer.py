from rest_framework import serializers
from hencasa.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['us_nombre','us_apellidos','us_edad','us_direccion','us_telefono','us_email','us_password','clsus_num_documento']