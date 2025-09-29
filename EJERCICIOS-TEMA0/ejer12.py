"""
Diseñar la función calculadora(), a la que se le pasan dos números reales
(operandos) y qué operación se desea realizar con ellos. Las operaciones
disponibles son sumar, restar, multiplicar o dividir. Estas se especifican 
mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación
y 4 para la división. La función devolverá el resultado de la operación mediante un número real.
"""

import math

#funcion de la suma
def sumar(num1, num2):
    return num1 + num2

#funcion de la resta
def restar(num1, num2):
    return max(num1, num2) - min(num1, num2)

#funcion de dividir
def dividir(num1, num2):
    return max(num1, num2) / min(num1, num2)

#funcion de multiplicar
def multiplicar(num1, num2):
    return num1 * num2

#calculadora
def calculadora(num1, num2):

    print("CALCULADORA")
    print("Selecciona una opción:")
    print("""   1- Sumar
                2- Restar
                3- Dividir
                4- Multiplicar""")
    respuesta = int(input("Introduzca su respuesta: "))

    if (respuesta == 1):
        print(sumar(num1, num2))
    elif (respuesta == 2):
        print(restar(num1, num2))
    elif (respuesta == 3):
        print(dividir(num1, num2))
    elif (respuesta == 4):
        print(multiplicar(num1, num2))

num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

calculadora(num1, num2)