'''
Escribe un programa que lea un numero natural natural n > 0
y a continuacion escriba en una lnea, separados por comas y terminando
en punto, los n primeros numeros primos cuya ultima cifra (por la dere-
cha) no sea un 7.
'''
numero = int(input())

lista_divisores = []
contador = 2
while len(lista_divisores) < numero:
    
    if (contador+3)%10 != 0:
        for i in range(2, contador+1):
            primo = True
            for j in range(2, 11):
                if i == j:                          
                    break;                              
                elif i%j == 0:                         
                    primo = False
                else:
                    continue
        if primo == True:
            lista_divisores.append(i)
    contador += 1
            
    
cadena_divisores = ", ".join(str(e) for e in lista_divisores)
print("{}.".format(cadena_divisores))