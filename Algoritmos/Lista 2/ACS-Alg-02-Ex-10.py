m = int(input("Digite seu número de matrícula: "))

ano = (m // 10000)

s = ((m % 10000) // 100) // 10

print("Ano da matricula: ",ano)
print("Semestre:",s)