def main():
    quant = int(input("Digite a quantidade de itens do pedido: "))
    result = calcularenvio(quant)
    print("O custo total para o envio é de R${:.2f}".format(result))

def calcularenvio(quant):
    resultado = 10.95 + (quant-1)*2.95
    return resultado

main()