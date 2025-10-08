class Articulo:

    IVA = 21

    #constructor
    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantosQuedan = cuantosQuedan
        self.IVA = Articulo.IVA

    #devuelve el precio de venta al público (PVP) con iva incluido
    def getPVP(self):

        precioVentaPublico = self.precio * Articulo.IVA / 100

        return precioVentaPublico

    #que devuelva el PVP con un descuento pasado como argumento
    def getPVPDescuento(self, descuento):

        precioConDescuento = Articulo.getPVP * descuento / 100

        return  precioConDescuento
    
    #se vende un objeto siempre que la cantidad a vender sea menor o igual
    #a la cantidad actual
    def vender(self, cantidadAVender):

        vendido = False

        if (self.cuantosQuedan >= cantidadAVender):
            self.cuantosQuedan -= cantidadAVender
            vendido = True

        return vendido
    
    #se almacena la cantidad que se pase por parametros siempre que
    #la cantidad sea mayor que 0 porque si no no tendría sentido
    def almacenar(self, cantidadAlmacenar):
        almacenado = False

        if (cantidadAlmacenar > 0):
            self.cuantosQuedan += cantidadAlmacenar
            almacenado = True

        return almacenado
    
    #método string
    def __str__(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.cuantosQuedan}"
    
    #método equals que determina que dos articulos son iguales cuando
    #tienen el mismo nombre
    def __eq__(self, otroObjeto):
        iguales = False

        if (self.nombre == otroObjeto.nombre):
            iguales = True

        return iguales
    
    #realiza una ordenacion dependiendo del nombre de los articulos
    def __lt__(self, otroObjeto):

        menor = False

        if (self.nombre < otroObjeto.nombre):
            menor = True

        return menor