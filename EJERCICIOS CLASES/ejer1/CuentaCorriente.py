#creación de clase
class CuentaCorriente:
    #se inicializa el nombre a una cadena vacía
    nombre = ""

    #creación de constructor
    def __init__(self, dni, saldo):
        self.nombre = ""
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

    #convierte el objeto en cadena
    def __str__(self):
        return "Nombre del titular: ", self.nombre, " | Saldo: ", str(self.saldo)
    
    #método equals que define que dos objetos son iguales si su dni es el mismo
    def __eq__(self, otroObjeto):
        iguales = False

        if (self.dni == otroObjeto.dni):
            iguales = True

        return iguales
    
    #método para realizar una ordenacion de menor a mayor dependiendo del saldo de cada cuenta
    def __lt__(self, otroObjeto):
        menor = False

        if (self.saldo < otroObjeto.saldo):
            menor = True
        
        return menor

    