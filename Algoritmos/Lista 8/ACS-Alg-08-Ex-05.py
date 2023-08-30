def somar_valores():
    valor = input("Digite um valor numérico (enter para parar): ")

    if valor == "":
        return 0.0
    else:
        try:
            numero = float(valor)
            soma_restante = somar_valores()
            return numero + soma_restante
        except ValueError:
            print("ERRO: Valor inválido.")
            return somar_valores()

soma_total = somar_valores()
print("A soma total dos valores é:", soma_total)