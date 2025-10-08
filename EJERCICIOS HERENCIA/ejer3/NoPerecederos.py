from Producto import *

class NoPerecederos(Producto):

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def calcular(self, numeroCantidad):
        return super().calcular(numeroCantidad)
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    def __lt__(self, otroObjeto):
        return super().__lt__(otroObjeto)