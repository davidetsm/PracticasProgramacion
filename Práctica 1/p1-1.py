'''Escribe un programa en Python que lea tres numeros enteros
y devuelva el mayor y el menor de ellos.
'''
lista_numeros = []

for i in range(3):
    numero = int(input("Introduce un número: "))
    lista_numeros.append(numero)

numero_mayor = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_mayor:
        numero_mayor = numero
        
numero_menor = lista_numeros[0]

for numero in lista_numeros:
    if numero < numero_menor:
        numero_menor = numero
        
print("El mayor es: {}.".format(numero_mayor))
print("El menor es: {}.".format(numero_menor))