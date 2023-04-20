n = int(input("Digite um número de três algarismos: "))

c = n // 100
r_1 = n % 100

d = r_1 // 10
u = r_1 % 10

print("Centena:", c, "\n Dezena:", d, "\n Unidade:", u)