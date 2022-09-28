from django.db import models
from .usuario import Usuario

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    fa_parentesco = models.TextField('parentesco', max_length=30)
    fa_correo = models.TextField('correo', max_length=30)
    usuario_fk = models.ForeignKey(Usuario, related_name='usuariofa', on_delete=models.CASCADE)