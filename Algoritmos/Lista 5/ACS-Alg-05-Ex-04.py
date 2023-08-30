def main():
    a = float(input("Digite um valor: "))
    b = float(input("Digite um valor: "))
    c = float(input("Digite um valor: "))
    resultado = fazermediana(a,b,c)
    print("A mediana dos valores recebidos é", resultado)



def fazermediana(a,b,c):
    maximo = max(a,b,c)
    minimo = min(a,b,c)
    mediana = (a+b+c)-minimo-maximo
    return mediana

main()