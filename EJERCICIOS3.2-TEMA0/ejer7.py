"""
Crea un programa que permita al usuario agregar,
eliminar y buscar contactos en una libreta de direcciones 
implementada como un diccionario. La clave del diccionario 
será el nombre del contacto y el valor, su número de teléfono. 
Crea un menú para las distintas opciones e implementa una 
función para cada opción
"""

diccionario = {}

#funcion para mostrar el menu
def mostrarMenu():
    print("""   MENÚ
                1- Agregar contacto
                2- Mostrar contacto
                3- Buscar contacto
                4- Eliminar contacto
                5- Salir""")
    return int(input("Introduzca su opción: "))

#funcion para agregar un contacto
def agregarContacto(clave, valor, diccionario):
    #se agrega al diccionario
    diccionario[clave] = valor

#funcion para mostrar los contactos
def mostrarContactos(diccionario):
    print(diccionario)

#buscar los contactos
def buscarContacto(clave, diccionario):
    seEncuentra : bool = True

    if (clave in diccionario):
        print(clave, diccionario[clave])
    else:
        seEncuentra = False

    return seEncuentra

#eliminar un contacto específico
def eliminarContacto(clave, diccionario):
    del diccionario[clave]

#variable para introducir una clave
def introducirClave():
    return input("Introduce el nombre del contacto: ")

#variable para introducir un valor
def introducirValor():
    return input("Introduce el número de contacto: ")

opcion = mostrarMenu()

while(opcion < 5):
    #si la opción es 1
    if (opcion == 1):
        #se agrega un contacto
        agregarContacto(introducirClave(), introducirValor(), diccionario)
    elif(opcion == 2):
        #llamo a la función
        mostrarContactos(diccionario)
    elif(opcion == 3):
        #busco un diccionario
        buscarContacto(introducirClave(), diccionario)
    elif(opcion == 4):
        eliminarContacto(introducirClave(), diccionario)

    opcion = mostrarMenu()