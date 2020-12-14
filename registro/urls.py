from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiante/new', views.estudiante_new, name='estudiante_new'),
    path('docentes/', views.docentes, name='docentes'),
    path('docente/new', views.docente_new, name='docente_new'),
]