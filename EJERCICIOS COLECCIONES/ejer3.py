"""
Realiza un programa que pida 8 números enteros y 
los almacene en una lista. A continuación, recorrerá 
esa tabla y mostrará esos números junto con la 
palabra “par” o “impar” según proceda
"""

#creo la lista
lista : int = []

#for para pedir un número 10 veces
for i in range(1, 10):

    #recojo el número
    num = int(input("Introduzca un número: "))

    #agrego el número a la lista
    lista.append(num)

#recorro la lista
for j in lista:
    #si el número es par muestra un mensaje indicandolo
    if (j % 2 == 0):
        print("El número es par.")
    else:
        print("El número es impar.")