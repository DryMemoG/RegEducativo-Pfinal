from django import forms
from .models import *
class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=('nombres', 'apellidos', 'fecha_nac','noCarnet','grado','seccion',)
        
class DocenteForm(forms.ModelForm):
    class Meta:
        model=Docente
        fields=('nombres', 'apellidos','noCarnet',)