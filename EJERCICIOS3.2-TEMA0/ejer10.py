"""
Crea un diccionario donde las claves sean 
el conjunto 1 de la siguiente tabla y los 
valores, el conjunto 2:
conjunto 1:

e i k m p q r s t u v
p v i u m t e r k q s

El programa debe pedir una frase al usuario y 
debe mostrar la frase encriptada. Para ello, cada 
vez que encuentre en la frase una letra del conjunto 
1 la sustituirá por su correspondiente en el conjunto 2
"""

#creacion del diccionario para codificar
diccionario = {"e": "p", "i": "v", "k": "i", "m": "u", "p": "m", "q": "t", "r": "e", "s": "r", "t": "k", "u": "q", "v": "s"}

#variable que almacena la frase que crea el usuario
frase = input("Introduzca una frase: ")

fraseCodificada = ""

#recorro la frase que ha introducido el usuario
for i in frase:

    #cojo la letra de la frase y compruebo si está en el diccionario
    if (i in diccionario):

        #a la frase codificada le concateno el valor de la letra ya que el valor es la codificación
        fraseCodificada += diccionario[i]
    #como en la codificación no están todas las letras, si no se encuentra se añade el mismo caracter
    else:
        fraseCodificada += i

    #aumento el contador
    contador += 1

print(fraseCodificada)