def fazerdicionario(palavra):
    dicionario = {}
    for i in palavra:
        if (i in dicionario) == True:
            dicionario[i] = dicionario[i] + 1
        else:
            dicionario[i] = 1
    return dicionario


def verificaranagrama(dicionario1, dicionario2):
    c1 = set(dicionario1.keys())
    c2 = set(dicionario2.keys())

    # testar se as strings nao contem letras diferentes
    if c1 != c2:
        return False

    # testar a quantidade de ocorrencias de cada letra
    for chave in dicionario1:
        if dicionario1[chave] != dicionario2[chave]:
            return False
    return True


def main():
    palavra1 = input("Digite a palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    d_a = fazerdicionario(palavra1)
    d_b = fazerdicionario(palavra2)
    print(d_a, len(d_a))
    print(d_b, len(d_b))
    print(verificaranagrama(d_a, d_b))


main()
