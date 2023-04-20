valor =int(input("Digite a quantidade em segundos: "))

dia = valor // 86400
s_d = valor % 86400

hora = s_d // 3600
s_h = s_d % 3600

minutos = s_h // 60
segundos = s_h % 60

print("Dia(s): ", dia)
print("Hora(s): ", hora)
print("Minuto(s): ", minutos)
print("Segundo(s): ", segundos)