from Punto import *

punto1 = Punto(5,1)
punto2 = Punto(4,9)
punto3 = Punto(0,5)
punto4 = Punto(0,32)

#recoge la distancia entre esos puntos
distancia1 = punto1.distancia(punto3)

print(distancia1)

punto2.setXY(54,2)

cadena1 = punto2.__str__()

print(cadena1)

