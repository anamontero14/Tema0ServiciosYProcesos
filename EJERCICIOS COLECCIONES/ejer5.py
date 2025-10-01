"""
Crea un programa que cree una lista de enteros de tamaño 100 
y lo rellene con valores enteros aleatorios entre 1 y 10. 
Luego pedirá un valor N y mostrará cuántas veces aparece N
"""

#importo la clase random con sus metodos
import random

#inicializo la lista
lista : int = []

for i in range(1,100):
    #a la variable que almacena los numeros enteros le indico
    #que se randomice en cada iteración con 1 número del 1 al 100
    numRandom = random.randint(1,101)

    #se mete el numero en la lista CON .APPEND
    lista.append(numRandom)

#pedir un valor
num = int(input("Introduce un número: "))

numeroVeces = lista.count(num)

#muestro el número de veces que se encuentra el valor introducido en la lista
print(numeroVeces)