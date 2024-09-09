class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad_maxima):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes_inscritos = []

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            print(f"Error: El estudiante {estudiante.nombre} ya está inscrito en el curso {self.nombre}.")
            return

        if len(self.estudiantes_inscritos) >= self.capacidad_maxima:
            print(f"Error: Curso {self.nombre} está lleno, no se puede inscribir a {estudiante.nombre}.")
            return

        self.estudiantes_inscritos.append(estudiante)
        estudiante.cursos_inscritos.append(self)
        print(f"Estudiante {estudiante.nombre} inscrito en el curso {self.nombre}.")

    def baja_estudiante(self, estudiante):
        if estudiante not in self.estudiantes_inscritos:
            print(f"Error: El estudiante {estudiante.nombre} no está inscrito en el curso {self.nombre}.")
            return

        self.estudiantes_inscritos.remove(estudiante)
        estudiante.cursos_inscritos.remove(self)
        print(f"Estudiante {estudiante.nombre} se dio de baja del curso {self.nombre}.")

    def __str__(self):
        return (f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor}, "
                f"Inscritos: {len(self.estudiantes_inscritos)}/{self.capacidad_maxima}")
