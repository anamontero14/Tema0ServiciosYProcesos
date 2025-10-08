class Empleado:

    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombreNuevo):
        self.nombre = nombreNuevo

    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        return "Empleado: " + self.nombre