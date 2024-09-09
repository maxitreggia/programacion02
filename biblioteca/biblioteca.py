from programacion02.biblioteca.libro import Libro
from programacion02.biblioteca.miembro import Miembro


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_miembro_por_id(self, id_miembro):
        for miembro in self.miembros:
            if miembro.id_miembro == id_miembro:
                return miembro
        return None

    def agregar_libro(self, titulo, autor, isbn, ejemplar):
        if self.buscar_libro_por_isbn(isbn):
            print(f"El libro con ISBN {isbn} ya existe en la biblioteca.")
        else:
            libro = Libro(titulo, autor, isbn, ejemplar)
            self.libros.append(libro)
            print(f"Libro '{titulo}' agregado a la biblioteca.")

    def agregar_miembro(self, nombre, id_miembro):
        if self.buscar_miembro_por_id(id_miembro):
            print(f"El miembro con ID {id_miembro} ya está registrado.")
        else:
            miembro = Miembro(nombre, id_miembro)
            self.miembros.append(miembro)
            print(f"Miembro '{nombre}' registrado en la biblioteca.")

    def consultar_estado_libros(self):
        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

    def consultar_estado_miembros(self):
        if not self.miembros:
            print("No hay miembros registrados en la biblioteca.")
        else:
            for miembro in self.miembros:
                print(miembro)

    def prestar_libro(self, id_miembro, isbn):
        miembro = self.buscar_miembro_por_id(id_miembro)
        libro = self.buscar_libro_por_isbn(isbn)
        if not miembro:
            print(f"No se encontró el miembro con ID {id_miembro}.")
            return
        if not libro:
            print(f"No se encontró el libro con ISBN {isbn}.")
            return
        if not libro.disponible:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
            return
        miembro.tomar_prestado(libro)

    def devolver_libro(self, id_miembro, isbn):
        miembro = self.buscar_miembro_por_id(id_miembro)
        libro = self.buscar_libro_por_isbn(isbn)
        if not miembro:
            print(f"No se encontró el miembro con ID {id_miembro}.")
            return
        if not libro:
            print(f"No se encontró el libro con ISBN {isbn}.")
            return
        miembro.devolver_libro(libro)
