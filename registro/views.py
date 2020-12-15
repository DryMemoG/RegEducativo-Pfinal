from django.shortcuts import render
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.
def inicio(request):
    estudiantes = Estudiante.objects.filter(fecha_nac__lte=timezone.now()).order_by('fecha_nac')
    return render(request, 'registro/inicio.html', { 'estudiantes': estudiantes})

#Vistas a Reads
def estudiantes(request):
    estudiantes = Estudiante.objects.filter(fecha_nac__lte=timezone.now()).order_by('fecha_nac')
    return render(request, 'registro/estudiantes.html', { 'estudiantes': estudiantes})
def docentes(request):
    docentes = Docente.objects.all().order_by('apellidos')
    return render(request, 'registro/docentes.html', { 'docentes': docentes})
def cursos(request):
    cursos = Curso.objects.all().order_by('grado')
    return render(request, 'registro/cursos.html',{'cursos': cursos})
def asignaciones(request):
    asignaciones = Asignacion.objects.all().order_by('curso')
    return render(request, 'registro/asignaciones.html', {'asignaciones':asignaciones})


#vistas a POST
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

def curso_new(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'registro/curso_edit.html', {'form': form})

def asignacion_new(request):
    if request.method == "POST":
        form = AsignacionForm(request.POST)
        if form.is_valid():
            asignacion = form.save(commit=False)
            asignacion.save()
            return redirect('asignaciones')
    else:
        form = AsignacionForm()
    return render(request, 'registro/asignacion_edit.html', {'form': form})