def main():
    numero = int(input("Digite o número que deseja verificar: "))
    resposta = verificar(numero)
    if resposta == False:
        print("O número inserido é par.")
    else:
        print("O número inserido é primo.")

def verificar(numero):
    resultado = numero % 2
    if resultado == 1:
        return True
    else:
        return False
    
main()