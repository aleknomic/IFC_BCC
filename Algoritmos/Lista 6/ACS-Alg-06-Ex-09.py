def fazermedia(lista):
    quant = len(lista)
    soma = 0
    media = 0
    for i in lista:
        soma = soma + i
    media = soma / quant
    return round(media, 2)

def valoresbaixos(i, media):
    if i < media:
        return True
    else:
        return False

def valoresacima(i,media):
    if i > media:
        return True
    else:
        return False

def valoresmedios(i,media):
    if i == media:
        return True
    else:
        return False

def main():
    l1 = []
    while True:
        x = input("Digite a nota (enter para parar): ")
        if x == "":
            break
        nota = float(x)
        l1.append(nota)
    med = fazermedia(l1)
    print("Média das notas:", med)
    print("Valores abaixo da média:")
    for i in l1:
        if valoresbaixos(i, med):
            print(i)
    print("Valores médios:")
    for i in l1:
        if valoresmedios(i,med):
            print(i)
    print("Valores acima da média:")
    for i in l1:
        if valoresacima(i,med):
            print(i)

main()