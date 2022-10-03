from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from hencasa.models.familiar import Familiar
from hencasa.serializers.familiarSerializer import FamiliarSerializer

class FamiliarDetailView(generics.ListCreateAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
     
    def list(self, request):
        print('lista todos los usuarios')
        queryset = self.get_queryset()
        serializer = FamiliarSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print('POST a usuarios')
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = usuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)