def countrange(lista, maximo, minimo):
    quant = 0
    for i in lista:
        if i >= minimo and i < maximo:
            quant = quant + 1
    return quant


def main():
    l1 = []
    while True:
        x = input("Digite um elemento de sua lista (enter para parar): ")
        if x == "":
            break
        numero = float(x)
        l1.append(numero)
    maximo = float(input("Digite o valor máximo: "))
    minimo = float(input("Digite o valor mínimo: "))
    print(countrange(l1, maximo, minimo))


main()
