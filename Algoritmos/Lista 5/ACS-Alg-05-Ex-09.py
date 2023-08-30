def main():
    string = input("Digite algo: ")
    resultado = isInteger(string)
    if resultado == True:
        print("Sua string é um inteiro.")
    else:
        print("Sua string não é um inteiro.")


def isInteger(string):
    string = string.strip()
    for i in string:
        if i == "+" or i == "-":
            continue
        i = ord(i)
        if i >= 48 and i < 58:
            return True
        else:
            return False


main()
