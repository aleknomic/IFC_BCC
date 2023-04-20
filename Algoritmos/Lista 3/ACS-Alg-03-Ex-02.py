anos = int(input("Digite a quantidade de anos: "))

if anos <= 0:
    print("ERRO")
elif anos >= 0 and anos <= 2:
    icanina = anos * 10.5
    print("Seu cachorro possui", icanina, "anos.")
else:
    icanina = 21 + ((anos - 2) * 4)
    print("Seu cachorro possui", icanina, "anos.")
