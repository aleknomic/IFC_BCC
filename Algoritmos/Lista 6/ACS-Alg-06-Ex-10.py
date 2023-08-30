def adicionare_e_virgula(lista):
    stringfinal = ""
    n = len(lista)
    for i in lista:
        if i != lista[n-2] and i != lista[n-1]:
            stringfinal = stringfinal + i + ", "
        if i == lista[n-2]:
            stringfinal = stringfinal + i + " e"
        if i == lista[n-1]:
            stringfinal = stringfinal + " " + i
    return stringfinal


def main():
    l1 = []
    while True:
        item = input("Digite um item de lista (enter para parar): ")
        if item == "":
            break
        l1.append(item)
       
    s_final = adicionare_e_virgula(l1)

    print(s_final)

main()