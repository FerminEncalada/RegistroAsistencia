class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.asistencias = {}

    def marcar_asistencia(self, asignatura, fecha, presente):
        if asignatura not in self.asistencias:
            self.asistencias[asignatura] = {}
        self.asistencias[asignatura][fecha] = presente


class Profesor:
    def __init__(self, nombre, apellido, asignatura):
        self.nombre = nombre
        self.apellido = apellido
        self.asignatura = asignatura


class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)


class PeriodoAcademico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
