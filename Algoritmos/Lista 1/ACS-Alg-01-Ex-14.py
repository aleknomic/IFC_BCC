l1 = int(input("Digite o valor do primeiro lado do triangulo: "))
l2 = int(input("Digte o valor do segundo lado do triangulo: "))
l3 = int(input("Digite o valor do terceiro lado do triangulo: "))

l = (l1 + l2 + l3) / 2

import math

area = math.pow(l *(l - l1) * (l - l2) * (l - l3), 1/2)

print("A area do triangulo é igual a", area)