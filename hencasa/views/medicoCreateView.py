from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from hencasa.models.medico import Medico
from hencasa.serializers.medicoSerializer import MedicoSerializer

class MedicoCreateView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
     
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = medicoSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)