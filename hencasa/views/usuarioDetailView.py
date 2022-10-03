from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from hencasa.models.usuario import Usuario
from hencasa.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioDetailView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
     
    def list(self, request):
        print('lista todos los usuarios')
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
    


