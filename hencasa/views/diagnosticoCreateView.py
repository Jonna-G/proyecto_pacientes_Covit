from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from hencasa.models.diagnostico import Diagnostico
from hencasa.serializers.diagnosticoSerializer import DiagnosticoSerializer

class DiagnosticoCreateView(generics.ListCreateAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
     
    def list(self, request):
        print('lista todos los usuarios')
        queryset = self.get_queryset()
        serializer = DiagnosticoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = diagnosticoSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)