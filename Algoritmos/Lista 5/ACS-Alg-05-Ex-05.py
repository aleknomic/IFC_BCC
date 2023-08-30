def main():
    x = int(input("Digite um valor: "))
    resposta = ordinal(x)
    print(resposta)

def ordinal(x):
    if x == 1:
        return "Primeiro"
    if x == 2:
        return "Segundo"
    if x == 3:
        return "Terceiro"
    if x == 4:
        return "Quarto"
    if x == 5:
        return "Quinto"
    if x == 6:
        return "Sexto"
    if x == 7:
        return "Sétimo"
    if x == 8:
        return "Oitavo"
    if x == 9:
        return "Nono"
    if x == 10:
        return "Décimo"
    if x == 11:
        return "Décimo primeiro"
    if x == 12:
        return "Décimo segundo"
    if x > 12 or x < 1:
        return ""

main()