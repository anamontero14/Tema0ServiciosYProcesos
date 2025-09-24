"""
Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
"""
import math

print("NUMERO PRIMO O NO")

#numero a ver si es primo o no
numeroIntroducir = int(input("Introduzca un número ENTERO POSITIVO: "))

#comprobar el resto de la division entre el numero y la raiz cuadrada
raizCuadrada = int(numeroIntroducir % math.sqrt(numeroIntroducir))

#comprobar si es divisible entre 2
divisible2 = int(numeroIntroducir % 2)

# si la raiz cuadrada dividida entre el numero y el numero dividido entre 2
# dan 0 significa que es primo
if (raizCuadrada == 0 and divisible2 == 0):
    print("El numero NO es primo")
else:
    print("El número ES primo")