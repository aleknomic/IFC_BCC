def tirarmaxemin(lista, n):
    return lista[n:-n]


def main():
    lista = []
    while True:
        x = input("Digite um número (digite enter para parar): ")
        if x == "":
            break
        numero = int(x)
        lista.append(numero)
    if len(lista) < 4:
        print("Sua lista tem menos de 4 objetos.")
    if len(lista) >= 4:
        n = int(
            input(
                "Digite a quantidade de vezes que deseja retirar o máximo e o mínimo da lista: "
            )
        )
        print(tirarmaxemin(lista, n))


main()
