from programacion02.facultad.curso import Curso
from programacion02.facultad.estudiante import Estudiante


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self, nombre, apellido, matricula, carrera):
        if any(estudiante.matricula == matricula for estudiante in self.estudiantes):
            print(f"Error: Ya existe un estudiante con la matrícula {matricula}.")
            return

        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(estudiante)
        print(f"Estudiante {nombre} {apellido} registrado con éxito.")

    def agregar_curso(self, nombre, codigo, profesor, capacidad_maxima):
        if any(curso.codigo == codigo for curso in self.cursos):
            print(f"Error: Ya existe un curso con el código {codigo}.")
            return

        curso = Curso(nombre, codigo, profesor, capacidad_maxima)
        self.cursos.append(curso)
        print(f"Curso {nombre} registrado con éxito.")

    def inscribir_estudiante_en_curso(self, estudiante_id, codigo_curso):
        estudiante = next((e for e in self.estudiantes if e.id == estudiante_id), None)
        curso = next((c for c in self.cursos if c.codigo == codigo_curso), None)

        if not estudiante:
            print(f"Error: Estudiante con ID {estudiante_id} no encontrado.")
            return
        if not curso:
            print(f"Error: Curso con código {codigo_curso} no encontrado.")
            return

        curso.inscribir_estudiante(estudiante)

    def baja_estudiante_de_curso(self, estudiante_id, codigo_curso):
        estudiante = next((e for e in self.estudiantes if e.id == estudiante_id), None)
        curso = next((c for c in self.cursos if c.codigo == codigo_curso), None)

        if not estudiante:
            print(f"Error: Estudiante con ID {estudiante_id} no encontrado.")
            return
        if not curso:
            print(f"Error: Curso con código {codigo_curso} no encontrado.")
            return

        curso.baja_estudiante(estudiante)

    def consultar_estado_cursos(self):
        if not self.cursos:
            print("No hay cursos registrados.")
        for curso in self.cursos:
            print(curso)

    def consultar_estado_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        for estudiante in self.estudiantes:
            print(estudiante)
