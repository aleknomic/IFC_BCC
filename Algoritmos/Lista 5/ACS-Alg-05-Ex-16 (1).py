def main():
    numero = input("Digite o número: ")
    baseA = int(input("Digite a base que seu número está: "))
    baseB = int(input("Digite a base para qual deseja converter: "))
    print(
        "Seu número convertido é",
        converte_baseA_baseB(numero, baseA, baseB),
        "na base",
        baseB,
    )


def int2hex(n):
    if n >= 0 and n <= 9:
        return str(n)
    if n == 10:
        return "A"
    if n == 11:
        return "B"
    if n == 12:
        return "C"
    if n == 13:
        return "D"
    if n == 14:
        return "E"
    if n == 15:
        return "F"


# recebe um caracter e retorna um inteiro
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
        return int(string)


def converte_b_para_decimal(numero, base):
    dec = 0
    # quantidade de caracteres da string de entrada
    n = len(numero)
    expoente = n - 1

    # para cada caracter da entrada, monta a parcela correspondente no somatorio para a conversao
    for i in range(n):
        dec = dec + hex2int(numero[i]) * base**expoente
        expoente = expoente - 1

    return dec


def converte_decimal_para_b(numero_decimal, base):
    resultado = ""
    while (numero_decimal // base) > 0:
        resto = numero_decimal % base
        resultado = int2hex(resto) + resultado
        numero_decimal = numero_decimal // base
        # print(numero_decimal)
    resultado = int2hex(numero_decimal) + resultado
    return resultado


def converte_baseA_baseB(numero, baseA, baseB):
    decimal = converte_b_para_decimal(numero, baseA)
    resultado = converte_decimal_para_b(decimal, baseB)
    return resultado


main()
