from django.contrib import admin
from .models.usuario import Usuario
from .models.paciente import Paciente
from .models.medico import Medico
from .models.auxiliar import Auxiliar
from .models.familiar import Familiar
from .models.historia_medica import Historia_medica
from .models.diagnostico import Diagnostico
from .models.asignacion import Asignacion

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(Historia_medica)
admin.site.register(Diagnostico)
admin.site.register(Asignacion)

# Register your models here.

