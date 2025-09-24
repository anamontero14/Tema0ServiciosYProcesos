#Pedir dos números y mostrarlos ordenados de menor a mayor.

#primer numero
numero1 = int(input("Introduce un número: "))

#segundo numero
numero2 = int(input("Introduce otro número: "))

if numero1 > numero2:
    print(numero2,numero1)
elif numero1 == numero2:
    print("Los números son iguales")
else:
    print(numero1,numero2)