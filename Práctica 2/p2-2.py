
def leerVector(n):
    v = [int(x) for x in input().split()]
    if len(v) != n:
        return None
    return v

def MayorMenor(n, v, w):
    for i in range(n): 
        if v[i] > w[i]:
            return 1
        elif v[i] < w[i]:
            return -1
    return 0

n = int(input())
v = leerVector(n)
w = leerVector(n)

while v == None and w == None:
    print("Vuelva a introducir los vectores")
    v = leerVector(n)
    w = leerVector(n)
    #Mantenemos la misma dimensión que la introducida al principio

print(MayorMenor(n, v, w))