import random

lista = []

while len(lista) < 6:
    n = random.randint(1, 60)
    if n not in lista:
        lista.append(n)

cresc = sorted(lista)
print(cresc)
