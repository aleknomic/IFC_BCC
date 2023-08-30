def retirarpontos_e_upper(frase):
    frasesempontos = ""
    for i in frase:
        if i == "," or i == "." or i == "!" or i == " " or i == "?":
            continue
        else:
            frasesempontos = frasesempontos + i
    frasefinal = frasesempontos.upper()
    return frasefinal


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
    if c1 != c2:
        return False
    for chave in dicionario1:
        if dicionario1[chave] != dicionario2[chave]:
            return False
    return True


def main():
    frase1 = input("Digite a primeira frase: ")
    frase2 = input("Digite a segunda frase: ")
    f1 = retirarpontos_e_upper(frase1)
    f2 = retirarpontos_e_upper(frase2)
    d_f1 = fazerdicionario(f1)
    d_f2 = fazerdicionario(f2)
    print(verificaranagrama(d_f1, d_f2))


main()
