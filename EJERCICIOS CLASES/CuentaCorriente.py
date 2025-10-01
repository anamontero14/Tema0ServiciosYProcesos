#creación de clase
class CuentaCorriente:
    #se inicializa el nombre a una cadena vacía
    nombre = ""

    #creación de constructor
    def __init__(self, dni, saldo):
        self.dni = dni
        self.saldo = saldo
    
    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    def sacarDinero(self, dineroSacar):
        #variable para controlar que se realiza la operación
        realizarOperacion = True

        if (self.saldo <= 0 and self.saldo >= dineroSacar):
            realizarOperacion = False
        #si el saldo no es 0 y la cantidad a sacar no
        #es mayor al saldo actual
        else:
            #se saca el dinero
            self.saldo -= dineroSacar
        #se devuelve true o false dependiendo de si la operación
        #fue o no exitosa
        return realizarOperacion

    def ingresarDinero(self, dineroIngresar):
        #se ingresa el dinero
        self.saldo += dineroIngresar

    