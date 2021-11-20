def leerMatriz(n, m):
    matriz = []
    for i in range(n):
        fila = [int(x) for x in input().split()]
        matriz.append(fila)
    return matriz

def matrizTraspuesta(n, m, matriz):
    matriz_traspuesta = []
    for i in range(m): #Creo una matriz n x m con todos sus elementos nulos
        fila = [0]*n 
        matriz_traspuesta.append(fila)
    #Tenemos claro que los elementos de la matriz traspuesta cambian n por m y viceversa
    for i in range(n):
        for j in range(m):
            matriz_traspuesta[j][i] = matriz[i][j]
    #Ahora la imprimimos
    for i in range(m):
        fila_matriz = " ".join(str(e) for e in matriz_traspuesta[i])
        print(fila_matriz)
    return matriz_traspuesta

def multiplicacion(n, m, matriz, matriz_traspuesta):
    matriz_multiplicacion = []
    #Llenamos la matriz con índices nulos 
    for i in range(n):
        fila = [0]*n
        matriz_multiplicacion.append(fila)
    #Calculamos los coeficientes
    for i in range(len(matriz_multiplicacion)):
        for j in range(len(matriz_multiplicacion[0])):
            sumatorio = 0
            for k in range(len(matriz_multiplicacion[0])+1):
                elemento = matriz[i][k]*matriz_traspuesta[k][j]
                sumatorio += elemento
            matriz_multiplicacion[i][j] = sumatorio
    print(" ")
    for i in range(n):
        fila_matriz = " ".join(str(e) for e in matriz_multiplicacion[i])
        print(fila_matriz)
    return matriz_multiplicacion

n = int(input())
m = int(input())
matriz = leerMatriz(n, m)
matriz_traspuesta = matrizTraspuesta(n, m, matriz)
multiplicacion(n, m, matriz, matriz_traspuesta)