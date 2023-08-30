def main():
    string = input(
        "Digite 1 único digito hexadecimal ou 1 número inteiro entre 0 a 15: "
    )
    if len(string) == 2:
        resposta = int2hex(string)
        print("Seu número inteiro convertido para um digito hexadecimal é", resposta)
    else:
        resposta = hex2int(string)
        print("Seu digito hexadecimal convertido para um número inteiro é", resposta)


def int2hex(string):
    if (
        string == "0"
        or string == "1"
        or string == "2"
        or string == "3"
        or string == "4"
        or string == "5"
        or string == "6"
        or string == "7"
        or string == "8"
        or string == "9"
    ):
        return string
    if string == "10":
        return "A"
    if string == "11":
        return "B"
    if string == "12":
        return "C"
    if string == "13":
        return "D"
    if string == "14":
        return "E"
    if string == "15":
        return "F"


def hex2int(string):
    if string == "A" or string == "a":
        return 10
    if string == "B" or string == "b":
        return 11
    if string == "C" or string == "c":
        return 12
    if string == "D" or string == "d":
        return 13
    if string == "E" or string == "e":
        return 14
    if string == "F" or string == "f":
        return 15
    if (
        string == "0"
        or string == "1"
        or string == "2"
        or string == "3"
        or string == "4"
        or string == "5"
        or string == "6"
        or string == "7"
        or string == "8"
        or string == "9"
    ):
        return string


main()
