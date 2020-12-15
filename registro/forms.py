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
    

class CursoForm(forms.ModelForm):
    class Meta: 
        model = Curso
        fields = ('codigo', 'nombre','docente', 'grado')
    
class AsignacionForm(forms.ModelForm):
    class Meta: 
        model = Asignacion
        fields =('cod', 'estudiate', 'curso', 'nota')
    
