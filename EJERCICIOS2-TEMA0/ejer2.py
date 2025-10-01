"""
Crea un programa que pida diez números reales por teclado, 
los almacene en una lista, y luego lo recorra para averiguar
el máximo y mínimo y mostrarlos por pantalla
"""

import math

#creo la lista
lista : int = []

#for para pedir un número 10 veces
for i in range(1, 10):

    #recojo el número
    num = int(input("Introduzca un número: "))

    #agrego el número a la lista
    lista.append(num)

#muestro el mayor y menor número que tiene la lista
print(max(lista))
print(min(lista))