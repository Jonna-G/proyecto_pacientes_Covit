from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from hencasa.models.asignacion import Asignacion
from hencasa.serializers.asignacionSerializer import AsignacionSerializer

class AsignacionDetailView(generics.ListCreateAPIView):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
     
    def list(self, request):
        print('lista todos los usuarios')
        queryset = self.get_queryset()
        serializer = AsignacionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = asignacionSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)