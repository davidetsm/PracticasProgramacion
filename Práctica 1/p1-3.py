'''
Escribe un programa que funcione como una calculadora de
bolsillo. El programa debe leer una expresion compuesta por numeros (co-
mo no se sabe si van a ser enteros o reales, se debe suponer que son reales),
y operadores aritmeticos, que termina con el caracter \=", y debe escribir
los resultados de cada operacion. Se supone (no es necesario comprobarlo)
que la expresion va a ser correcta y que no va a tener espacios en blanco.
Los operadores que pueden aparecer son los cuatro operadores aritmeti-
cos: \+", \-", \*" y \/". Ten en cuenta que la division debe ser siempre
real.
'''
num1 = float(input())
operacion = input()

while operacion != "=":
    num2 = float(input())
    if operacion == ("+"):
        suma = num1 + num2
        print(suma)
        num1 = suma
    if operacion == ("-"):
        resta = num1 - num2
        print(resta)
        num1 = resta
    if operacion == ("*"):
        multiplicacion = num1 * num2
        print(multiplicacion)
        num1 = multiplicacion
    if operacion == ("/"):
        division =  num1 / num2
        print(division)
        num1 = division
    operacion = input()