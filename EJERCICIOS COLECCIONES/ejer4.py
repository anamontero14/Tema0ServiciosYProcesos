"""
Escribe un programa que lea 10 números 
por teclado y que luego los muestre ordenados 
de mayor a menor.
"""

#creo la lista
lista : int = []

#for para pedir un número 10 veces
for i in range(1, 10):

    #recojo el número
    num = int(input("Introduzca un número: "))

    #agrego el número a la lista
    lista.append(num)

#primero ordeno la lista al revés (mayor a menor)
lista.sort(reverse=True)

#muestro la lista ordenada de mayor a menor
print(lista)