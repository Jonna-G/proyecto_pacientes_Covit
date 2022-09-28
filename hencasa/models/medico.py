from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    med_especializacion = models.TextField('especializacion', max_length=30)
    med_registro = models.TextField('registro', max_length=30)
    usuario_fk = models.ForeignKey(Usuario, related_name='usuariome', on_delete=models.CASCADE)