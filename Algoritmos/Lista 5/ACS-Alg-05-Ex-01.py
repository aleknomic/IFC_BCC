def main():
    b = float(input("Digite o valor do primeiro comprimento menor: "))
    c = float(input("Digite o valor do segundo comprimento menor: "))
    pit = pitagoras(b, c)
    result = hip(pit)
    print("O valor da hipotenusa é", result)

def pitagoras(b, c):
    resultado = (b ** 2) + (c ** 2)
    return resultado

def hip(pit):
    hipotenusa = pit ** (1/2)
    return hipotenusa

main()