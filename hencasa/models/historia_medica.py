from django.db import models
from .paciente import Paciente

class Historia_medica(models.Model):
    id_Historiamed = models.AutoField(primary_key=True)
    hi_oximetria = models.TextField('oximetria', max_length=30)
    hi_glisemia = models.TextField('glisemia', max_length=30)
    hi_presionart = models.TextField('presionart', max_length=30)
    hi_frecuenciares = models.TextField('frecuenciares', max_length=30)
    hi_temperatura = models.TextField('temperatura', max_length=30)  
    paciente_fk = models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)

