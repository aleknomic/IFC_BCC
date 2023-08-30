def buscaReversa(dicionario, numerobusca):
    lista = []
    for x in dicionario:
        valor = dicionario.get(x)
        if valor == numerobusca:
            lista.append(x)
    return lista


def main():
    d1 = {}
    while True:
        chave = input("Digite o nome da chave (enter para parar): ")
        if chave == "":
            break
        numero = int(input("Digite o número da chave: "))
        d1[chave] = numero
    buscando = int(input("Digite a chave que deseja buscar: "))
    print(buscaReversa(d1, buscando))


main()
