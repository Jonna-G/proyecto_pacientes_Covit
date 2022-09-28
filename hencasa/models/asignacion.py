from django.db import models
from .auxiliar import Auxiliar
from .paciente import Paciente
from .medico import Medico

class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    paciente_fk = models.ForeignKey(Paciente, related_name='pacienteasi', on_delete=models.CASCADE)
    medico_fk = models.ForeignKey(Medico, related_name='medicoasi', on_delete=models.CASCADE)