def leeVector():
    v = [int(x) for x in input().split()]
    return v

def cortarVector(v, p, l):
    if 0 <= p <= (len(v)-1) and (p + l) <= len(v):
        v = v[p:p+l]
        return v
    else:
        return "error"

def imprimirVector(v):
    for x in v:
        print(x, end = " ")
    print()

v = leeVector()
p = int(input())
l = int(input())

if 0 <= p <= (len(v)-1) and (p + l) <= len(v):
    v = v[p:p+l]
    imprimirVector(v)
else:
    print("error")