"""
Diseña un programa que registre las ventas de una 
tienda en un diccionario, donde las claves son los 
nombres de los productos y los valores son las 
cantidades vendidas. El programa debe permitir al 
usuario agregar nuevas ventas y calcular el total de 
ventas para un producto específico. Implementa un 
menú con ambas opciones
"""

diccionario = {}

#funcion para mostrar el menu
def mostrarMenu():
    print("""   MENÚ
                1- Agregar producto
                2- Calcular el total de venta
                3- Salir""")
    return int(input("Introduzca su opción: "))

#funcion para agregar un contacto
def agregarProducto(clave, valor, diccionario):
    #se agrega al diccionario
    diccionario[clave] = valor

#buscar ventas
def buscarVentas(clave, diccionario):
    seEncuentra : bool = True

    if (clave in diccionario):
        print(clave, diccionario[clave])
    else:
        seEncuentra = False

    return seEncuentra

#variable para introducir una clave
def introducirClave():
    return input("Introduce el nombre del producto: ")

#variable para introducir un valor
def introducirValor():
    return input("Introduce la cantidad de ventas del producto: ")

opcion = mostrarMenu()

while(opcion < 3):
    #si la opción es 1
    if (opcion == 1):
        #se agrega un contacto
        agregarProducto(introducirClave(), introducirValor(), diccionario)
    elif(opcion == 2):
        buscarVentas(introducirClave(), diccionario)

    opcion = mostrarMenu()