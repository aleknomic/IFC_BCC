def listardivisores(numero):
    lista = []
    i = 1
    while i <= numero:
        if numero % i == 0:
            lista.append(i)
        i = i + 1
    return lista


def main():
    numero = int(input("Digite o número inteiro positivo: "))
    print("Os divisores do número", numero, "são:")
    for e in listardivisores(numero):
        print(e)


main()
