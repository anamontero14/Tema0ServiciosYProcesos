class Libro:

    #constructor con todos los parametros obligatorios
    def __init__(self, tituloLibro, autor, numEjemplares, numEjemplaresPrestados):
        self.tituloLibro = tituloLibro
        self.autor = autor
        self.numEjemplares = numEjemplares
        self.numEjemplaresPrestados = numEjemplaresPrestados

    def prestamo(self):

        prestado = False

        #si quedan por lo menos uno o mas ejemplares significa
        #que si que se puede hacer un prestamo
        if (self.numEjemplares >= 1):
            self.numEjemplaresPrestados += 1
            self.numEjemplares -= 1
            prestado = True
        
        return prestado
    
    def devolucion(self):

        devuelto = False

        #si el numero de ejemplares prestados es mayor o igual a 1 entonces
        #significa que como se ha prestado un ejemplar se podrá también
        #devolver
        if (self.numEjemplaresPrestados >= 1):
            self.numEjemplares += 1
            self.numEjemplaresPrestados -= 1
            devuelto = True

        return devuelto
    
    #metodo string
    def __str__(self):
        return "Título: " + self.tituloLibro + " | Autor: " + self.autor + " | Número de ejemplares: " + str(self.numEjemplares) + " | Número de ejemplares prestados: " + str(self.numEjemplaresPrestados)
    
    #metodo equals
    def __eq__(self, otroObjeto):
        
        iguales = False

        #los libros se consideran iguales si tienen el mimso titulo y el
        #mismo autor
        if (self.tituloLibro == otroObjeto.tituloLibro and self.autor == otroObjeto.autor):
            iguales = True

        return iguales
    
    #metodo de ordenacion
    def __lt__(self, otroObjeto):

        menor = False

        if (self.autor > otroObjeto.autor):
            menor = True

        return menor
    
