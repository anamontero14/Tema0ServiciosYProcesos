"""
Escribe un programa que vaya pidiendo al usuario números 
enteros positivos que debe ir sumando. 
Cuando el usuario no quiera insertar más números, 
introducirá un número negativo y el algoritmo, 
antes de acabar, mostrará la suma de los números 
positivos introducidos por el usuario.
"""

#variable para almacenar la suma de los numeros
suma = 0

#variable para almacenar el número que va introduciendo el usuario
numero = int(input("Introduce un número: "))

while (numero >= 0):
    #se le suma el numero a la variable suma
    suma += numero
    #se recoge otra vez el numero
    numero = int(input("Introduce un número: "))

#se anuncia el fin del bucle y el resultado de la suma
print("Fin del bucle, la suma de todos los números es: ", suma)