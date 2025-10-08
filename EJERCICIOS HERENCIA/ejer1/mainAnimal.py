from Animal import *
from Perro import *
from Gato import *

#objetos
perro = Perro("Tonto", 4)
gato = Gato("Piripi", 4)

cadena1 = perro.__str__()
cadena2 = gato.__str__()

cadena3 = perro.habla()

print(cadena3)
print(cadena1)
print(cadena2)
