from django.contrib import admin
from .models import Estudiante, Asignatura, RegistroAsistencia

admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(RegistroAsistencia)
