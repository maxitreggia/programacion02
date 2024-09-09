class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.prestar(self)
            self.libros_prestados.append(libro)
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro '{libro.titulo}' no puede ser devuelto porque no fue prestado por este miembro.")

    def __str__(self):
        libros = ', '.join(libro.titulo for libro in self.libros_prestados) if self.libros_prestados else 'ninguno'
        return f"Miembro: {self.nombre} (ID: {self.id_miembro}) - Libros prestados: {libros}"
