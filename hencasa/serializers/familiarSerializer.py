from rest_framework import serializers
from hencasa.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['id_familiar','fa_parentesco','fa_correo','usuario_fk']