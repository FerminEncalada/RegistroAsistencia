from django.shortcuts import render
from .models import Estudiante, Asignatura, RegistroAsistencia

def tomar_asistencia(request):
    if request.method == 'POST':
        # Lógica para tomar la asistencia y guardarla en la base de datos
        return redirect('tomar_asistencia')  # Redirigir a la página de tomar asistencia nuevamente
    else:
        estudiantes = Estudiante.objects.all()
        asignaturas = Asignatura.objects.all()
        return render(request, 'tomar_asistencia.html', {'estudiantes': estudiantes, 'asignaturas': asignaturas})

def ver_asistencias(request):
    asistencias = RegistroAsistencia.objects.all()
    return render(request, 'ver_asistencias.html', {'asistencias': asistencias})

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')