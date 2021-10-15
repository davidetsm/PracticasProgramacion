'''
Escribe un programa que lea un numero natural natural n > 0
y a continuacion lea n numeros enteros y escriba la media aritmetica 
del cuadrado de dichos numeros con dos cifras decimales.
'''

cantidad = int(input("Introduce la cantidad de números a leer: "))
suma = 0
for i in range(0, cantidad):
    num = int(input("Introduce el número {}: ".format(i+1)))
    num_elevado = num**2
    suma += num_elevado

media = suma/cantidad
media_dos_decimales = round(media, 2)
print(media_dos_decimales)