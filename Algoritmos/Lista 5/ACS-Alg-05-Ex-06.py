def main():
    frase = input("Digite a frase que deseja centralizar: ")
    espaco = int(input("Digite a largura da linha: "))
    centralizado = centralizar(frase,espaco)
    linha = '-' * espaco
    print(linha)
    print(centralizado)

def centralizar(frase, espaco):
    resultado = frase.center(espaco)
    return resultado

main()