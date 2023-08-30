def raiz_quadrada(n, estimativa):
    diferenca = abs(estimativa ** 2 - n)
    
    if diferenca <= 1e-12:
        return estimativa
    else:
        nova_estimativa = (estimativa + n / estimativa) / 2
        return raiz_quadrada(n, nova_estimativa)

numero = float(input("Digite um número: "))
est = 1.0

if numero < 0:
    print("ERRO: O número deve ser não negativo.")
else:
    resultado = raiz_quadrada(numero, est)
    print("A raiz quadrada de", numero, "é:", resultado)