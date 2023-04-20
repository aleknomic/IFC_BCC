n = float(input("Digite a quantidade de vasilhames de um litro ou menos: "))
m = float(input("Digite a quantidade de vasilhames de mais de um litro: "))

menoslitro = n * 0.10
maislitro = m * 0.25
total = menoslitro + maislitro

print("Valor total dos créditos a receber: R$ %.2f" % (total))