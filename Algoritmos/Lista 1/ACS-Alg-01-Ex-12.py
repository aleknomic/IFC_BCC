r = float(input("Digite o raio da circunferencia: "))

import math

area = round((math.pi * r**2))
volume = (4 * math.pi * r**3) / 3

print("A área dessa circunferencia é:", area)
print("e seu volume é:", volume)