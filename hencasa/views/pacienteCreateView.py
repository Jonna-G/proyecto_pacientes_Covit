from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from hencasa.models.paciente import Paciente
from hencasa.serializers.pacienteSerializer import PacienteSerializer

class PacienteCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
     
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = usuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)