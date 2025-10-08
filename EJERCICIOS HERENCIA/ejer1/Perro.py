from Animal import *

class Perro(Animal):
    
    #constructor heredado
    def __init__(self, nombre, numPatas):
        super().__init__(nombre, numPatas)

    def habla(self):
        return "Guau"
    
    def __str__(self):
        return "Soy un perro | " + super().__str__()