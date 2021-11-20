from math import sqrt

def leerVector():
    vector = [float(x) for x in input().split()]
    return vector

def leerMatriz(n):
    matriz = []
    for i in range(n):
        fila = [float(x) for x in input().split()]
        matriz.append(fila)
    return matriz

def distanciaEuclidea(vector, fila):
    v = vector
    for i in range(len(v)):
        v[i] = vector[i] - fila[i]
    suma = 0
    for i in range(len(vector)):
        elemento = (v[i])**2
        suma += elemento
    distancia = sqrt(suma)
    return distancia

def imprimirVector(fila):
    for i in fila:
        print(i, end = " ")
    print()

n = int(input())
m = int(input())
vector = leerVector()
matriz = leerMatriz(m)

distanciaMinima = distanciaEuclidea(vector, matriz[0])
indice = 0
for i in range(1, len(matriz)):
    distancia_nueva = distanciaEuclidea(vector, matriz[i])
    if distancia_nueva < distanciaMinima:
        distanciaMinima = distancia_nueva
        indice = i
imprimirVector(matriz[indice])