"""
Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
"""
import math

def maximo(num1, num2):
    return max(num1, num2)

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))

print(maximo(num1, num2))