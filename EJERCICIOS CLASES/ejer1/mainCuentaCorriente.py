from CuentaCorriente import *


objeto = CuentaCorriente("24564564K", 10002)

cadena = objeto.__str__()

print(cadena)

objeto.ingresarDinero(20)

cadena = objeto.__str__()

print(cadena)

objeto.sacarDinero(300)

cadena = objeto.__str__()

print(cadena)