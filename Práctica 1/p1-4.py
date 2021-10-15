'''
Escribe un programa que lea un numero natural n > 0 y mues-
tre todos sus divisores primos, exceptuando el 1 y el propio numero, sepa-
rados por comas y 
nalizando en punto. Si no encuentra ninguno debera
mostrar el mensaje \El numero n es primo.".
'''

numero = int(input("Introduce un número: "))

numeros_primos=[]

i = 1

'''Vamos a calcular los n primeros numeros primos
y los incluimos en una lista que usaremos posteriormente'''
for i in range(2, numero+1):
    
    primos = True
    for j in range(2, 11):
        if i == j:                          
            break;                              
        elif i%j == 0:                         
            primos = False
        else:
            continue
    if primos == True:
        numeros_primos.append(i)
#print(numeros_primos)

lista_divisores = []

if numero in numeros_primos:
    print("El número {} es primo.".format(numero))
else:
    for k in numeros_primos:
        if numero % k == 0:
            lista_divisores.append(k)
#print(lista_divisores)
    cadena_divisores = ", ".join(str(e) for e in lista_divisores)

    print("{}.".format(cadena_divisores))    