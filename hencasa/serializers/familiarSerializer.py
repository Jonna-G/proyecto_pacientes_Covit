from rest_framework import serializers
from hencasa.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields='__all__'
