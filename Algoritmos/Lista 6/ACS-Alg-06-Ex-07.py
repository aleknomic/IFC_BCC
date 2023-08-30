def listardivisores(numero):
    lista = []
    i = 1
    while i < numero:
        if numero % i == 0:
            lista.append(i)
        i = i + 1
    return lista


def eh_perfeito(n):
    soma = 0
    divisores = listardivisores(n)
    for numero in divisores:
        soma = soma + numero
    if soma == n:
        return True
    else:
        return False


def main():
    for i in range(1, 10000):
        if eh_perfeito(i):
            print(i)


main()
