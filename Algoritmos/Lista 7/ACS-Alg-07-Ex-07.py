import random


def criarlista_B(lista):
    while len(lista) < 5:
        n = random.randint(1, 15)
        if n not in lista:
            lista.append(n)
    return lista


def criarlista_I(lista):
    while len(lista) < 5:
        n = random.randint(16, 30)
        if n not in lista:
            lista.append(n)
    return lista


def criarlista_N(lista):
    while len(lista) < 5:
        n = random.randint(31, 45)
        if n not in lista:
            lista.append(n)
    return lista


def criarlista_G(lista):
    while len(lista) < 5:
        n = random.randint(46, 60)
        if n not in lista:
            lista.append(n)
    return lista


def criarlista_O(lista):
    while len(lista) < 5:
        n = random.randint(61, 75)
        if n not in lista:
            lista.append(n)
    return lista


def main():
    lista = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    listaB = criarlista_B(lista)
    listaI = criarlista_I(lista1)
    listaN = criarlista_N(lista2)
    listaG = criarlista_G(lista3)
    listaO = criarlista_O(lista4)
    tabela = {}
    tabela["B"] = listaB
    tabela["I"] = listaI
    tabela["N"] = listaN
    tabela["G"] = listaG
    tabela["O"] = listaO
    print("B\tI\tN\tG\tO")
    for i in tabela:
        string = ""
        for numero in tabela[i]:
            numerostr = str(numero)
            string = string + numerostr + "\t"
        print(string)


main()
