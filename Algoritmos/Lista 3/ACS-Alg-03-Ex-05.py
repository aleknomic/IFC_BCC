mês = input("Digite o nome do mês: ")

if mês==("fevereiro"):
    print("Esse mês possui 28 ou 29 dias.")
elif mês==("abril") or mês==("junho") or mês==("setembro") or mês==("novembro"):
    print("Esse mês possui 30 dias.")
else:
    print("Esse mês possui 31 dias.")
    