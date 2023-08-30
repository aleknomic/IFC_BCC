def main():
    c1 = float(input("Digite um comprimento: "))
    c2 = float(input("Digite um comprimento: "))
    c3 = float(input("Digite um comprimento: "))
    if verificar1(c1,c2,c3) <= c1:
        print("Não é possível formar um triângulo.")
    elif verificar2(c1,c2,c3) <= c2:
        print("Não é possível formar um triângulo.")
    elif verificar3(c1,c2,c3) <= c3:
        print("Não é possível formar um triângulo.")
    else:
        print("É possível formar um triângulo.")

def verificar1(c1,c2,c3):
    valor1 = c2 + c3
    return valor1

def verificar2(c1,c2,c3):
    valor2 = c1 + c3
    return valor2

def verificar3(c1,c2,c3):
    valor3 = c1 + c2
    return valor3

main()