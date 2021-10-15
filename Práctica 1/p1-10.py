'''
Se puede demostrar (lo vereis en breve en la asignatura de
Analisis) que
ex = 1 + x +
x2
2!
+
x3
3!
+    +
xn
n!
+    =
1X
n=0
xn
n!
Implementa un programa que pida al usuario un numero real y calcule ex
mediante la serie anterior. El calculo debe parar cuando la diferencia entre
el valor actual y el anterior sea menor que 10􀀀6. El resultado se mostrara,
por tanto, con 6 cifras decimales.
'''
from math import factorial, e

num = float(input())

error = 10**-6
sumatorio = 1
contador = 1
valor = 1 #Le doy un valor inicial cualquiera mayor que el error.
while valor >= error:
    
    valor = num**(contador)/factorial(contador)
    valor_antes = num**(contador-1)/factorial(contador-1)
    contador += 1
    sumatorio += valor
    
sumatorio_redondeado = round(sumatorio, 6)

print(sumatorio_redondeado)
print(e**num)