def main():
    mes = int(input("Digite o mês (em número): "))
    ano = int(input("Digite o ano: "))
    print("O mês", mes, "no ano", ano, "possui", verificar(mes,ano), "dias.")

def verificar(mes,ano):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    if mes == 2:
        if ano % 400 == 0 or ano % 4 == 0:
            return 29
        else:
            return 28
        
main()