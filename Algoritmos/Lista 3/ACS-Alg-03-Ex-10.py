coluna = input("Digite a letra da coluna: ")
numero = int(input("Digite o número da posição: "))

if coluna == ("a") or coluna == ("c") or coluna == ("e") or coluna == ("g"):
    if numero % 2 == 0:
        print("QUADRADO PRETO")
    else:
        print("QUADRADO BRANCO")
if coluna == ("b") or coluna == ("d") or coluna == ("f") or coluna == ("h"):
    if numero % 2 != 0:
        print("QUADRADO BRANCO")
    else:
        print("QUADRADO PRETO")
