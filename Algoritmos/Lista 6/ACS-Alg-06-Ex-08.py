def verificarfrase(frase):
    l1 = frase.split()
    l2 = []
    for i in l1:
        nova_palavra = ""
        for caractere in i:
            if caractere.isalpha():
                nova_palavra = nova_palavra + caractere
        l2.append(nova_palavra)
    return l2


def main():
    frase = input("Digite uma frase: ")
    resultado = verificarfrase(frase)
    print(resultado)


main()
