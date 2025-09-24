"""
Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.
"""

print("APRENDER A CONTAR")

#pedir al usuario un numero
numero = int(input("Introduce un número: "))

#for que imprime todos los numeros desde el 1 hasta el numero especificado
for contador in range(1, numero + 1):
    print(contador)