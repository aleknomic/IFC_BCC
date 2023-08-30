def precedencia(x):
    if x == "+" or x == "-":
        return 1
    if x == "*" or x == "/":
        return 2
    if x == "^":
        return 3
    else:
        return -1


def main():
    operador = input("Digite o operador que deseja verificar a precedência: ")
    resposta = precedencia(operador)
    if resposta >= 1:
        print(resposta)
    else:
        print("ERRO: um operador não foi digitado.")


main()
