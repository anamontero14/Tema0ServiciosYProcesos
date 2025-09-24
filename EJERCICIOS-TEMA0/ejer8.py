"""
Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
"""

print("TRIANGULO")

#introducir un numero para hacer la piramide
numTriangulo = int(input("Introduce el numero para crear una pirámide: "))

for i in range(1, numTriangulo+1):
    print(" " * int(numTriangulo - i), "* " * int(i))