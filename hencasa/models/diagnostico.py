from django.db import models
from .usuario import Usuario
from .historia_medica import Historia_medica

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    dia_sugerencias = models.TextField('sugerencias', max_length=30)
    dia_fecha = models.DateField ()
    hismedico_fk = models.ForeignKey(Historia_medica, related_name='historia_medica', on_delete=models.CASCADE)