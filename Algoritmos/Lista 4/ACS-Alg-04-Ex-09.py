x = int(input("Digite um número: "))

raiz = x / 2
diferença = (raiz*raiz)-x

while diferença < 0.000000000001:
    raiz = (raiz + (x / raiz)) / 2

print(raiz)