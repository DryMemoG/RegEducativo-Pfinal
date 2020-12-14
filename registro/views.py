from django.shortcuts import render
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.
def inicio(request):
    estudiantes = Estudiante.objects.filter(fecha_nac__lte=timezone.now()).order_by('fecha_nac')
    return render(request, 'registro/inicio.html', { 'estudiantes': estudiantes})
    
def estudiantes(request):
    estudiantes = Estudiante.objects.filter(fecha_nac__lte=timezone.now()).order_by('fecha_nac')
    return render(request, 'registro/estudiantes.html', { 'estudiantes': estudiantes})
def docentes(request):
    docentes = Docente.objects.all().order_by('apellidos')
    return render(request, 'registro/docentes.html', { 'docentes': docentes})

def estudiante_new(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.save()
            return redirect('estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'registro/estudiante_edit.html', {'form': form})

def docente_new(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            docente = form.save(commit=False)
            docente.save()
            return redirect('docentes')
    else:
        form = DocenteForm()
    return render(request, 'registro/docente_edit.html', {'form': form})
