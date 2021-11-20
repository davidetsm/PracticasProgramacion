from math import sqrt

def leerMatriz(n):
    matriz = []
    for i in range(n):
        fila = [int(x) for x in input().split()]
        matriz.append(fila)
    return matriz

def mediaDiagonal(matriz, n):
    sumatorio = 0
    for i in range(len(matriz[0])):
        elemento_diagonal = matriz[i][i]
        sumatorio += elemento_diagonal
    media = sumatorio / n
    return media
        
def maximoDiagonal(matriz, n):
    maximo = matriz[0][n-1] #Supongo máximo el elemento de la ultima fila
    for i in range(len(matriz)):
        nuevo_maximo = matriz[n-i-1][i]
        if nuevo_maximo > maximo:
            maximo = nuevo_maximo
    return maximo

def distanciaEuclidea(matriz, n):
    if n%2 == 0:
        v1 = matriz[int(n/2)]
        v2 = matriz[int((n/2)+1)]
        v3 = v1 #Le asigno un vector de la misma dimension. Da igual el que sea porque luego le cambio el coeficiente
        for i in range(len(matriz)): #Como n es igual por filas y columnas da igual
            v3[i] = v1[i] - v2[i]
        sumatorio = 0
        for i in range(len(v3)):
            elemento = (v3[i])**2
            sumatorio += elemento
        distancia = sqrt(sumatorio)
        if distancia / int(distancia) == 1:
            return(int(distancia))
        return distancia
    if n%2 != 0:
        v1 = matriz[(3//2)+1]
        v2 = matriz[3//2]
        v3 = v1
        for i in range(len(matriz)):
            v3[i] = v1[i] - v2[i]
        sumatorio = 0
        for i in range(len(v3)):
            elemento = (v3[i])**2
            sumatorio += elemento
        distancia = sqrt(sumatorio)
        if distancia / int(distancia) == 1:
            return int(distancia)
        return distancia


n = int(input()) #Numero de filas que tiene la matriz
matriz = leerMatriz(n)
print(mediaDiagonal(matriz, n))
print(maximoDiagonal(matriz, n))
print(round(distanciaEuclidea(matriz, n), 5))