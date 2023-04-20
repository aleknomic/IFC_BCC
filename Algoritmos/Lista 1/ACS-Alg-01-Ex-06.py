suco = float(input("Digite o valor do suco: "))
pp = float(input("Digite o valor do prato principal: "))
sm = float(input("Digite o valor da sobremesa: "))

total = suco + pp + sm

print("Valor total da refeição: R$ %.2f" % (total + total * 0.10))