"""
Crea un diccionario donde las claves son las 
letras del abecedario y los valores, la puntuación 
para cada letra, como en el Scrabble. El programa 
le pedirá una palabra al usuario y se mostrará por 
pantalla la puntuación que tiene la palabra en total
"""

import random

#creacion del diccionario
diccionario = {}

#lista de letras en las que se divide la palabra del usuario
letras = []

#contador
contador = 0

#puntuacion del usuario
puntosUsuario = 0

#lista de las letras del abecedario
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#diccionario
for letra in lista:
    #le asigno una puntuacion random a la variable
    puntuacion = random.randint(1,11)
    #agrego la letra
    diccionario[letra] = puntuacion

#pedir una palabra al usuario
palabrita = input("Introduzca una palabra: ")

#separo la palabra
for l in palabrita:
    letras.append(palabrita[contador:contador+1])

    contador += 1

for i in letras:
    #le sumo la puntuacion a los puntos del usuario
    puntosUsuario += diccionario[i]

print("Puntuación del usuario: ", puntosUsuario)