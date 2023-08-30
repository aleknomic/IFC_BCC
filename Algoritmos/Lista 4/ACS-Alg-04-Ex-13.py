n = int(input("Digite o número inteiro: "))
fator = 2

if n < 2:
    print("ERRO: o valor digitado é menor que 2!")

#Enquanto fator é menor que o número dado
while fator <= n:
    #se o resto da divisão di número atual pelo fator atual for igual a zero
    if n % fator == 0:
    #o valor do número vai ser substituido pela divisão do número anterior dividido pelo fator atual
        n = n / fator

        #printa o fator atual
        print(fator)
        #E volta para o começo
        continue

    #se o resto da divisão do núemro atual pelo faotr atual for diferente de 0
    if n % fator != 0:
        #faotr receberá mais 1
        fator = fator + 1

    #se o fator for par:
    if fator % 2 == 0:
        #fator recebe mais 1
        fator = fator + 1

