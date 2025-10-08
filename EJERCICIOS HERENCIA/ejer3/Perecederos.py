from Producto import *

class Perecederos(Producto):

    def __init__(self, nombre, precio, diasCaducar):
        super().__init__(nombre, precio)

        self.diasCaducar = diasCaducar

    def calcular(self, numeroCantidad):
        return super().calcular(numeroCantidad)

    def reducirPrecio(self):
        if(self.diasCaducar == 1):
            self.precio /= 4
        elif(self.diasCaducar == 2):
            self.precio /= 3
        elif(self.diasCaducar == 3):
            self.precio /= 2

    def __eq__(self, value):
        return super().__eq__(value)
    
    def __lt__(self, otroObjeto):
        return super().__lt__(otroObjeto)