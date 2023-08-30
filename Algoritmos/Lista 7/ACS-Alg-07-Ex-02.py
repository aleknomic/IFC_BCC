def diferenca(c1, c2):
    uniao = c1.union(c2)
    inter = c1.intersection(c2)
    return uniao.difference(inter)


def main():
    conjunto1 = set()
    conjunto2 = set()
    while True:
        n = input("Digite um número do primeiro conjunto (enter para terminar): ")
        if n == "":
            break
        n = int(n)
        conjunto1.add(n)
    while True:
        a = input("Digite um número do segundo conjunto (enter para parar): ")
        if a == "":
            break
        a = int(a)
        conjunto2.add(a)
    print(diferenca(conjunto1, conjunto2))


main()
