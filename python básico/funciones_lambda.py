lista = [1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def pares(x):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares


print(pares(lista))


pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)


def try_again(effort: int):
    print("Better")


effort = 1
success = False
while not success:
    try_again(effort=+2)
