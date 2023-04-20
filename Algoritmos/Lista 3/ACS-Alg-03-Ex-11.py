a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

discriminante = ((b ** 2) - (4 * (a * c)))

if discriminante < 0:
    print("A equação não possui raízes.")
elif discriminante == 0:
    raiz = -b / (2 * a)
    print("O valor da única raíz da equação é:", raiz)
else:
    raiz1 = (-b + (discriminante ** 0.5)) / (2 * a)
    raiz2 = (-b - (discriminante ** 0.5)) / (2 * a)
    print("Os valores da equação são", raiz1, "e", raiz2)
