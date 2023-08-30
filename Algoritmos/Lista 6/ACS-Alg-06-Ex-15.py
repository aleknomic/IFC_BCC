def tokenizacao(n):
    lista = []
    anterior = ""
    numero = ""
    for elemento in n:
        if (
            (elemento == "(")
            or (elemento == ")")
            or (elemento == "*")
            or (elemento == "/")
            or (elemento == "^")
        ) or (
            (elemento == "+" or elemento == "-")
            and (anterior.isnumeric() or anterior == ")")
        ):
            if numero != "":
                lista.append(numero)
                numero = ""
            lista.append(elemento)
        else:
            numero += elemento
        anterior = elemento
    if numero != "":
        lista.append(numero)
        numero = ""
    return lista


def main():
    n = input("Digite uma expressão matematica: ")
    token = tokenizacao(n)
    print(token)


main()
