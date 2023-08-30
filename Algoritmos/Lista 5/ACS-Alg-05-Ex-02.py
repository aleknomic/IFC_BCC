def main():
    valorinicial = 4
    m = converterkmparam()
    valor_t = calcularcorrida(valorinicial, m)
    print("O valor total da corrida é R${:.2f}".format(valor_t))

def converterkmparam():
    quilometros = float(input("Digite a quantidade de quilometros percorridos: "))
    valor = (quilometros * 1000)
    return valor

def calcularcorrida(valorinicial, m):
    resultado = valorinicial + ((m/140)*0.25)
    return resultado

main()