from rest_framework import serializers
from hencasa.models.historia_medica import Historia_medica

class HistoriamedicaSerializers(serializers.ModelSerializer):
     class Meta:
        model=Historia_medica
        fields='__all__'

