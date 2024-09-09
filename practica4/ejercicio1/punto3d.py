class Punto3D:
    def __init__(self, x=0, y=0, z=0):
        """Inicializa un punto en 3D. Si no se especifican coordenadas, se inicializa en el origen (0, 0, 0)."""
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """Devuelve una representación en cadena del punto."""
        return f"Punto en 3D: ({self.x}, {self.y}, {self.z})"
