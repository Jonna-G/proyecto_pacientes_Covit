"""Hospitalizacionencasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hencasa import views

urlpatterns = [
    path('user/', views.UsuarioDetailView.as_view()),
    path('paciente/', views.PacienteCreateView.as_view()),
    path('medico/', views.MedicoCreateView.as_view()),
    path('familiar/', views.FamiliarCreateView.as_view()),
    path('pacientelist/', views.PacienteDetailView.as_view()),
    path('asignacion/', views.AsignacionCreateView.as_view()),
    path('asignacionlist/', views.AsignacionDetailView.as_view()),
    path('historia/', views.HistoriamedicaCreateView.as_view()),
    path('historialist/', views.HistoriamedicaDetailView.as_view()),
]