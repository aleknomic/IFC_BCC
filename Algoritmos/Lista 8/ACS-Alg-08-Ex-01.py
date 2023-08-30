def fatorial(n): 
    if n == 1: 
        return 1 
    else: 
        return n*fatorial(n-1)

def main():
    numero = int(input("Digite o número que deseja calcular: "))
    print("O fatorial de", numero, "é igual a", fatorial(numero)) 

main()