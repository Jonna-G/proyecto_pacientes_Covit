from django.db import models
from .usuario import Usuario

class Auxiliar(models.Model):
    id_auxiliar = models.AutoField(primary_key=True)
    au_descripcionasig = models.TextField('descripcionasig', max_length=30)
    usuario_fk = models.ForeignKey(Usuario, related_name='usuarioau', on_delete=models.CASCADE)