from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiante/new', views.estudiante_new, name='estudiante_new'),
    path('estudiante/<int:pk>/edit/', views.estudiante_edit, name='estudiante_edit'),
    path('estudiante/<pk>/delete/', views.estudiante_delete, name='estudiante_delete'),
    path('docentes/', views.docentes, name='docentes'),
    path('docente/new', views.docente_new, name='docente_new'),
    path('docente/<int:pk>/edit/', views.docente_edit, name='docente_edit'),
    path('docente/<pk>/delete/', views.docente_delete, name='docente_delete'),
    path('cursos/', views.cursos, name='cursos'),
    path('curso/new', views.curso_new, name='curso_new'),
    path('curso/<int:pk>/edit/', views.curso_edit, name='curso_edit'),
    path('curso/<pk>/delete/', views.curso_delete, name='curso_delete'),
    path('asignaciones/', views.asignaciones, name='asignaciones'),
    path('asignacion/new', views.asignacion_new, name='asignacion_new'),
    path('asignacion/<int:pk>/edit/', views.asignacion_edit, name='asignacion_edit'),
]