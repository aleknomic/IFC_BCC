import math

#  180  = pi
#   x   = ang_rad
#

t1_g = float(input("Digite a latitude do primeiro ponto: "))
g1_g = float(input("Digite a longitude do primeiro ponto: "))
t2_g = float(input("Digite a latitude do segundo ponto: "))
g2_g = float(input("Digite a longitude do segundo ponto: "))
t1_rad = (math.pi * t1_g) /180
g1_rad = (math.pi * g1_g) /180
t2_rad = (math.pi * t2_g) /180
g2_rad = (math.pi * g2_g) /180

distance = 6371.01 * math.acos(math.sin(t1_rad)) * math.sin(t2_rad) * math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad)

print("A distância entre os dois pontos é de: ", distance, "em quilometros")