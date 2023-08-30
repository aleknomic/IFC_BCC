def MDC(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return MDC(b,c)

def main():
    n1 = int(input("Digite um número inteiro positivo: "))
    n2 = int(input("Digite outro número inteiro positivo: "))
    print("o máximo divisor comum dos números", n1, "e", n2, "é", MDC(n1,n2))

main()