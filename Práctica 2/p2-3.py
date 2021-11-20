def leeVector():
    v = [int(x) for x in input().split()]
    return v

def ordenaVector(v):
    for j in range(len(v)):
        menor = v[j]
        posicion = j
        for i in range(j, len(v)):
            if v[i] < menor:
                menor = v[i]
                posicion = i
        variable = v[posicion]
        v[posicion] = v[j]
        v[j] = variable 
            
    return v

def imprimirVector(v):
    for x in v:
        print(x, end = " ")
    print()

v = leeVector()
ordenaVector(v)
imprimirVector(v)