class Estudiante:
    _id = 1  # Contador para generar identificador único

    def __init__(self, nombre, apellido, matricula, carrera):
        self.id = Estudiante._id
        Estudiante._id += 1
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos_inscritos = []

    def __str__(self):
        return (f'ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Matrícula: {self.matricula}, '
                f'Carrera: {self.carrera}, Cursos Inscritos: {[curso.nombre for curso in self.cursos_inscritos]}')
