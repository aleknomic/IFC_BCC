dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total = (((dias * 24) * 60) * 60) + ((horas * 60) * 60) + (minutos * 60) + segundos

print("A quantidade total de segundos deste intervalo de tempo é", total)