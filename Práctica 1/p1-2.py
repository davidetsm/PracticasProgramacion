'''
Un numero perfecto es un numero natural que es igual a la
suma de sus divisores propios positivos (consideramos que 1 es un divisor
propio, pero el propio numero no lo es). Asi, 6 es un numero perfecto
porque sus divisores propios son 1, 2 y 3; y 6 = 1 + 2 + 3. Escribe un
programa que lea un numero natural n > 0 y decida si es perfecto o no.
'''
numero = int(input("Introduce un número: "))

lista_divisores = []

i = 1
while i < numero:
    if numero % i == 0:
        lista_divisores.append(i)
    i += 1

if sum(lista_divisores) == numero:
    print("{} es un número perfecto.".format(numero))
else:
    print("{} no es un número perfecto.".format(numero))