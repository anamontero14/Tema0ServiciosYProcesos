from Libro import *

objeto = Libro("Filetes empanados", "Yo mismo", 67, 34)

cadena = objeto.__str__()

print(cadena)

objeto.prestamo()

cadena = objeto.__str__()

print(cadena)

objeto.devolucion()
objeto.devolucion()

cadena = objeto.__str__()

print(cadena)