class Libro:
    def __init__(self, titulo, autor, isbn, ejemplar):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplar = ejemplar
        self.disponible = True
        self.prestado_a = None

    def prestar(self, miembro):
        if self.disponible:
            self.disponible = False
            self.prestado_a = miembro
            print(f"El libro '{self.titulo}' ha sido prestado a {miembro.nombre}.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if not self.disponible:
            print(f"El libro '{self.titulo}' ha sido devuelto por {self.prestado_a.nombre}.")
            self.disponible = True
            self.prestado_a = None
        else:
            print(f"El libro '{self.titulo}' ya está disponible y no necesita ser devuelto.")

    def __str__(self):
        estado = "disponible" if self.disponible else f"prestado a {self.prestado_a.nombre}"
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {estado}"
