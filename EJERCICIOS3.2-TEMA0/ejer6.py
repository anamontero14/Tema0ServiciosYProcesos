"""
Escribe un programa que tome una cadena de texto como 
entrada y genere un diccionario que cuente la frecuencia 
de cada palabra en el texto
"""

#variable para almacenar la cadena de texto
cadena = input("Introduce una cadena de texto: ")

lista = []

#diccionario de palabras
diccionario = {}

#almaceno las palabras en el diccionario
lista = cadena.split()

#se recorre la lista de las cadenas
for i in lista:
    #el diccionario almacena como clave la palabra y como valor la longitud de la palabra
    diccionario[i] = len(i)

#se muestra el diccionario
print(diccionario)