"""
Escribe una función a la que se le pasen dos enteros y muestre 
todos los números comprendidos entre ellos. Desde el método main() 
lee los dos números enteros, los cuales deben introducirlos el usuario, 
y pásalos como parámetros de entrada de la función.
"""

def numeros_comprendidos(numero1:int, numero2:int):
    if (numero1 > numero2):
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1
    
    for i in range (menor, mayor + 1):
        print(i, end=",")
    

print("FUNCION")

#introducir los 2 numeros
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

numeros_comprendidos(numero1, numero2)