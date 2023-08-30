def verificarclassificacao(lista):
    if len(lista) == 1:
        return True
    ordenada = sorted(lista)
    if lista == ordenada:
        return True
    else:
        return False


def main():
    l1 = []
    while True:
        x = input("Digite um dos elementos da lista (enter para parar): ")
        if x == "":
            break
        numero = float(x)
        l1.append(numero)
    print(verificarclassificacao(l1))


main()
