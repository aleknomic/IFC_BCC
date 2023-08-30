def verificardata_magica(dia, mes, ano):
    ult_2_digitos = str(ano)[-2:]
    if int(dia * mes) == int(ult_2_digitos):
        return True
    return False


def main():
    diaInicio = 1
    mesInico = 1
    anoInico = 1901
    diaFim = 31
    mesFim = 12
    anoFim = 2000

    for ano in range(1901, 2000):
        for mes in range(1, 12):
            for dia in range(1, 31):
                if verificardata_magica(dia, mes, ano):
                    print(f"{dia}/{mes}/{ano}")


main()
