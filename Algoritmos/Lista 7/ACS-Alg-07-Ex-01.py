def verificar(conjunto):
    conjunto2 = set(conjunto)
    if len(conjunto2) == len(conjunto):
        return True
    else:
        return False


def main():
    frase = input("Digite sua frase: ")
    str1 = list(frase)
    print(verificar(str1))


main()
