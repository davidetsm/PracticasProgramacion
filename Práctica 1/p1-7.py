'''
Escribe un programa que vaya pidiendo numeros positivos y
menores o iguales que 100 al usuario y, cuando este termine (para lo cual
escribira 0), imprima la media geometrica de todos ellos con tres cifras
decimales (sin incluir el 0). Las numeros que no cumplan la condicion 0 <
x  100 se deben ignorar para calcular la media geometrica (incluyendo
el 0, obviamente). La media geometrica se calcula con la expresion
'''
from math import *

num = float(input("Introduce un número: "))
contador = 0
producto = 1
while num != 0:
    if num > 0 and num <= 100:
        producto *= num
        num = float(input("Introduce un número: "))
        contador += 1
    elif num > 100:
        num = float(input("Introduce un número: "))
    elif num < 0:
        num = float(input("Introduce un número: "))

media_geometrica = producto**(1/contador)
media_geometrica_redondeada = round(media_geometrica, 3)
print(media_geometrica_redondeada)