from django.db import models

# Create your models here.
class Grado(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Seccion(models.Model):
    seccion = models.CharField(max_length=2)
    
    def __str__(self):
        return self.seccion

class Estudiante(models.Model):
    nombres= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    fecha_nac= models.DateField()
    noCarnet= models.CharField(max_length=10)
    grado= models.ForeignKey(Grado, related_name='GradoEst', on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, related_name='Sección', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.noCarnet

class Docente(models.Model):
    nombres= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    noCarnet= models.CharField(max_length=10)
    
    def __str__(self):
        return self.noCarnet

class Curso(models.Model):
    codigo= models.CharField(max_length=25)
    nombre=models.CharField(max_length=50)
    docente = models.ForeignKey(Docente, related_name='Docente', on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, related_name='Grado',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigo
        
class Asignacion(models.Model):
    cod = models.CharField(max_length=25)
    estudiate= models.ForeignKey(Estudiante, related_name='Estudiante', on_delete=models.CASCADE)
    curso= models.ForeignKey(Curso, related_name='Curso',on_delete=models.CASCADE)
    nota = models.CharField(max_length=3)
    def __str__(self):
        return self.cod
