from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from hencasa.models.historia_medica import Historia_medica
from hencasa.serializers.historiamedicaSerializer import HistoriamedicaSerializer

class HistoriamedicaDetailView(generics.ListCreateAPIView):
    queryset = Historia_medica.objects.all()
    serializer_class = HistoriamedicaSerializer
     
    def list(self, request):
        print('lista todos los usuarios')
        queryset = self.get_queryset()
        serializer = HistoriamedicaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = historiamedicaSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)