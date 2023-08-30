def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
def main():
    numero = int(input("Digite o número: "))
    print("O", numero,"° termo da sequência de Fibonacci é", fibonacci(numero))

main()