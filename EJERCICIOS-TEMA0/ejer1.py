#Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

#Variable que almacena el dato que introduce el usuario CASTEANDOLO
numero = int(input("Introduzca un número para saber si es par o impar: "))

if numero % 2 == 0:
    print("Tu número es PAR")
else:
    print("Tu número es IMPAR")