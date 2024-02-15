from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos necesarios

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos necesarios

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    # Otros campos necesarios
