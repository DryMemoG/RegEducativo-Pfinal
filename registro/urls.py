from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiante/new', views.estudiante_new, name='estudiante_new'),
    path('docentes/', views.docentes, name='docentes'),
    path('docente/new', views.docente_new, name='docente_new'),
    path('cursos/', views.cursos, name='cursos'),
    path('curso/new', views.curso_new, name='curso_new'),
    path('asignaciones/', views.asignaciones, name='asignaciones'),
    path('asignacion/new', views.asignacion_new, name='asignacion_new'),
]