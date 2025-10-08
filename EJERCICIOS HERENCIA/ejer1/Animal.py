class Animal:

    #constructor
    def __init__(self, nombre, numPatas):
        self.nombre = nombre
        self.numPatas = numPatas

    def habla(self):
        return ""
    
    def __str__(self):
        return "Me llamo "+ self.nombre + ", tengo " + self.numPatas + " patas y sueno así: " + Animal.habla()
    
    