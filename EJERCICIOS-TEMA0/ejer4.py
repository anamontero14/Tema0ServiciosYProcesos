"""
Codificar el juego “el número secreto”, que consiste en acertar un 
número entre 1 y 100 (generado aleatoriamente). Para ello se introduce 
por teclado una serie de números, para los que se indica: “mayor” o “menor”, 
según sea mayor o menor con respecto al número secreto. El proceso 
termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
"""
import random

#numero generado aleatoriamente
numeroAleatorio = random.randint(1,101)

#el usuario intenta adivinar el numero
numeroUsuario = int(input("Introduce un número para inentar acertar: "))

#mientras que el numero introducido no sea negativo
while(numeroUsuario >= 0 and numeroUsuario != numeroAleatorio):
    #se comprueba si es mayor o menor que el aleatorio para darle una pista
    if (numeroUsuario > numeroAleatorio):
        print("MAYOR que el número secreto")
    else:
        print("MENOR que el número secreto")
    #se le pregunta por otro número
    numeroUsuario = int(input("Introduce otro número para inentar acertar: "))

#se comprueba si ha ganado o no
if (numeroAleatorio == numeroUsuario):
    print("HAS GANADO")

#se acaba el juego
print("Fin del juego")