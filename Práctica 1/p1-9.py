'''
La sucesion de Fibonnaci es una serie innita de numeros na-
turales donde cada elemento n  1 se obtiene de la siguiente forma:
fn =

n 􀀀 1 n  2
fn􀀀1 + fn􀀀2 n > 2
Escribe un programa que lea un numero natural n > 0 y a continuacion
escriba los n primeros numeros de dicha serie, separados por comas y
terminando en punto.
'''
num = int(input("Introduce un número: "))

numeros_sucesion = []
if num <= 2 and num > 0:
    for i in range (1,num+1):
        variable = i - 1
        numeros_sucesion.append(variable)     
if num > 2:
    n1 = 0
    numeros_sucesion.append(n1)
    n2 = 1
    numeros_sucesion.append(n2)
    for j in range(2, num):
        variable = n1 + n2
        numeros_sucesion.append(variable)
        n1 = n2
        n2 = variable


cadena_sucesion = ", ".join(str(e) for e in numeros_sucesion) 
print("{}.".format(cadena_sucesion))