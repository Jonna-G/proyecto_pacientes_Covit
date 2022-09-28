from django.db import models
from .usuario import Usuario

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    pa_direccion = models.TextField('direccion', max_length=30)
    pa_ciudad = models.TextField('ciudad', max_length=30)
    pa_fechaNacimiento = models.DateField ()    
    usuario_fk = models.ForeignKey(Usuario, related_name='usuariopa', on_delete=models.CASCADE)


