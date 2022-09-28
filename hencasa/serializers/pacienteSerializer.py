from rest_framework import serializers
from hencasa.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Usuario'] = UsuarioSerializer(instance.Usuario).data
        return response

