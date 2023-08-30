valorinicial = 4.95

print("Preço\t\tDesconto\t\tPreço c/ desconto")

while valorinicial < 25:
    print("R${:.2f}\t\t{}\t\t\tR${:.2f}".format(valorinicial, "60%", valorinicial * 0.6))
    valorinicial = valorinicial + 5

