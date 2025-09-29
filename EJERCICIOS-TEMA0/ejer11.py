"""
Crear una función que devuelva un tipo booleano que indique si el carácter que 
se pasa como parámetro de entrada corresponde con una vocal.
"""

def comprobar_letra (parametro1):

    esVocal = False

    parametro = parametro1.lower()

    if (parametro == "a" or parametro == "e" or parametro == "i" or parametro == "o" or parametro == "u"):
        esVocal = True
    
    return esVocal

letra = input("Introduce una letra: ")

if (comprobar_letra(letra)):
    print("La letra es vocal")
else:
    print("La letra no es vocal")