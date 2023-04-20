n = int(input("Digite o número de lados do poligono regular: "))
l = float(input("digite o comprimento de um dos lados: "))

import math

area = (n * (l**2)) / (4 * math.tan(math.pi/n))

print("A area do seu poligono regular é: ", area)