lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")
    