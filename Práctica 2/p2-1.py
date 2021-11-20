
def media(lista):
    suma = 0
    for i in lista:
        suma += i
    return (suma/len(lista))

def desviacion(lista):
    sumatorio = 0
    med = media(lista)
    for i in lista:
        sumatorio += (i-med)**2
    return ((sumatorio/(len(lista)-1))**0.5)

def moda(lista):
    modaa = lista[0]
    frecuencia_modaa = lista.count(modaa)
    for i in range(1, len(lista)):
        if lista.count(lista[i]) > frecuencia_modaa:
            modaa = lista[i]
            frecuencia_modaa = lista.count(lista[i])
    return modaa

def lista_valores():
    return [int(c) for c in input().split()]
    

lista = lista_valores()
print(round(media(lista), 5))
print(round(desviacion(lista), 5))
print(round(moda(lista), 5))