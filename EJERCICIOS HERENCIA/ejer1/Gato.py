from Animal import *

class Gato(Animal):

    #se llama al constructor del padre
    def __init__(self, nombre, numPatas):
        super().__init__(nombre, numPatas)

    def habla(self):
        return "Miau"
    
    def __str__(self):
        return "Soy un gato | " + super().__str__()