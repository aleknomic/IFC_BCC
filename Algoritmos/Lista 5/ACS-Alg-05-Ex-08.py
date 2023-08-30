def main():
    frase = input("Digite a frase: ")
    x = verificarletra(frase)
    print("A frase corrigida é", x)


def verificarletra(frase):
    # inicia o resultado
    frase2 = ""
    # len(frase) irá contar quantos caracteres tem na string (comprimento da frase)
    # for i in range(len(frase)) irá pegar cada letra de 0 a 4 na frase
    for i in range(len(frase)):
        # primeira letra da frase
        if i == 0:
            frase2 = (
                frase2 + frase[i].upper()
            )  # .upper() irá tornar o caracter i na frase (frase[i]) em letra maíscula
        elif i == 1:
            frase2 = frase2 + frase[i]
        else:
            ant1 = frase[i - 1]  # irá pegar o caracter anterior do atual
            ant2 = frase[i - 2]  # irá pegar o caracter anterior do anterior do atual
            # quando deve ser maiusculo
            if ant1 == " " and (ant2 == "!" or ant2 == "." or ant2 == "?"):
                frase2 = frase2 + frase[i].upper()
            else:
                frase2 = frase2 + frase[i]
    return frase2


main()
