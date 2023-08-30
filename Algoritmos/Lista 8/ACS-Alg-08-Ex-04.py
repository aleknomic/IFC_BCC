dicionario = {0:0 , 1:1}

def fibonacci(n):
    if n in dicionario:
        return dicionario[n]
    resultado = fibonacci(n-1) + fibonacci(n-2)
    dicionario[n] = resultado
    return resultado

def main():
    numero = int(input("Digite o número: "))
    print("O", numero,"° termo da sequência de Fibonacci é", fibonacci(numero))
    
main()