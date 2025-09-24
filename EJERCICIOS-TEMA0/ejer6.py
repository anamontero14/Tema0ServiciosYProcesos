"""
Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
"""

print("FACTORIAL DE UN NÚMERO")

#se le pide un numero al usuario
numero = int(input("Introduce un número para saber el factorial: "))

#creo el factorial
factorial = numero

#adivinar el factorial
#cuenta regresivamente desde UN NUMERO MENOS que
#el numero de 1 en 1
for multiplicar in range(numero - 1, 0, -1):
    #y cada numero lo va multiplicando por el factorial y asignandolo
    factorial *= multiplicar

print("El factorial de ", numero, " es ", factorial)