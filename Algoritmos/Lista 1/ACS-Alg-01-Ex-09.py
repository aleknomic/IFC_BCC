dinicial = float(input("Digite o depósito inicial: "))

#1ano
rendimento1 = dinicial * (0.12)
saldo1 = rendimento1 + dinicial
print("O rendimento do primeiro ano é R$ {:.2f}".format(rendimento1), "e o saldo é R$ {:.2f}".format(saldo1))

#2ano
rendimento2 = saldo1 * (0.12)
saldo2 = rendimento2 + saldo1
print("O rendimento do segundo ano é R$ {:.2f}".format(rendimento2), "e saldo é R$ {:.2f}".format(saldo2))

#3ano
rendimento3 = saldo2 * (0.12)
saldo3 = rendimento3 + saldo2
print("O rendimento do segundo ano é R$ {:.2f}".format(rendimento3), "e saldo é: R$ {:.2f}".format(saldo3))
