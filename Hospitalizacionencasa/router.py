from hencasa.viewsets import UsuarioViewsets
from hencasa.viewsets import PacienteViewsets
from hencasa.viewsets import MedicoViewsets
from hencasa.viewsets import FamiliarViewsets
from rest_framework import routers

router=routers.DefaultRouter()
router.register('usuario',UsuarioViewsets)
router.register('paciente',PacienteViewsets)
router.register('medico',MedicoViewsets)
router.register('familiar',FamiliarViewsets)