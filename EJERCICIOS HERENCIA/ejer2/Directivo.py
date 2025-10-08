from Empleado import *

class Directivo(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + "-> Directivo"