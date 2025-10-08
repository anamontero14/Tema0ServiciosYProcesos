import math

class Punto:
    #constructor con todos los parametros
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #método string
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    #setter de ambos atributos
    def setXY(self, xNueva, yNueva):
        self.x = xNueva
        self.y = yNueva
        
    #los puntos se desplazan tanto como se le indique por parámetros
    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy
    
    #calcula y devuelve la distancia entre el propio objeto y el punto indicado
    def distancia(self, punto):
        if (self.y == 0 and punto.y == 0):
            distancia = self.x - punto.x
        elif (self.x == 0 and punto.x == 0):
            distancia = self.y - self.y
        else:
            distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)

        return distancia