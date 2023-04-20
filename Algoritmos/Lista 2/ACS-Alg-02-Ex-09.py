data = int(input("Digite a data no formato DDMMAA: "))

dia = data // 10000
mes = (data % 10000) // 100

ano = data % 100

invertida= (ano * 10000) + (mes * 100) + dia

print("A data invertida é:", invertida)