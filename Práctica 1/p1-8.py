num = int(input())
contador_espacios = 0
espacio = " "

for i in range(num, 0, -1):
    print(contador_espacios*espacio, end="")
    for k in range(i, 0, -1):
        print(k, end="")
    for k in range(2, i+1):
        print(k, end="")
    print(contador_espacios*espacio)
    contador_espacios += 1

contador_espacios = num-2
for i in range(2, num+1):
    print(contador_espacios*espacio, end="")
    for k in range(i, 0, -1):
        print(k, end="")
    for k in range(2, i+1):
        print(k, end="")
    print(contador_espacios*espacio)
    contador_espacios -= 1