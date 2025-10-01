"""
Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 
"""

#importar random
import random

lista = list()

for i in range(1,10):
    #a la variable que almacena los numeros enteros le indico
    #que se randomice en cada iteración con 1 número del 1 al 100
    numRandom = random.randint(1,101)

    #se mete el numero en la lista CON .APPEND
    lista.append(numRandom)

#una vez termine hago que se muestre la lista
print(lista)