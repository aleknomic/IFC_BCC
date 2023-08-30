valortotal = 0

while True:
    resposta = input("Digite a idade da pessoa: ")
    if resposta == "":
        break
    idade = int(resposta)
    if idade <= 2:
        valortotal = valortotal
    if idade <= 12 and idade > 2:
        valortotal = valortotal + 14
    if idade > 13 and idade < 65:
        valortotal = valortotal + 23
    if idade >= 65:
        valortotal = valortotal + 18

print("O preço total das entradas é R$ {:.2f}".format(valortotal))
