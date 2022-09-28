from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from hencasa.models.usuario import Usuario
from hencasa.models.paciente import Paciente
from hencasa.models.medico import Medico
from hencasa.models.familiar import Familiar
from hencasa.serializers.usuarioSerializer import UsuarioSerializer
from hencasa.serializers.pacienteSerializer import PacienteSerializer
from hencasa.serializers.medicoSerializer import MedicoSerializer
from hencasa.serializers.familiarSerializer import FamiliarSerializer

class UsuarioViewsets(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PacienteViewsets(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewsets(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class FamiliarViewsets(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer