from rest_framework import serializers
from hencasa.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id_medico','med_especializacion','med_registro','usuario_fk']