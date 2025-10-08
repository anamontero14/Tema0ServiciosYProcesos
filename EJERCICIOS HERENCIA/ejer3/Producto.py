class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular(self, numeroCantidad):
        return self.precio * numeroCantidad
    
    def __str__(self):
        return "Nombre: " + self.nombre + " Precio: " + str(self.precio)
    
    def __lt__(self, otroObjeto):
        menor = False

        if (self.nombre < otroObjeto.nombre):
            menor = True

        return menor