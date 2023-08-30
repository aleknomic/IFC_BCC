def decbiniterativo(decimal):
    resultado = ""
    while decimal > 0:
        resto = decimal % 2
        resultado = str(resto) + resultado
        decimal = decimal//2
    return resultado

def main():
    q = int(input("Digite o número decinal que deseja converter: "))
    print(decbiniterativo(q))

main()