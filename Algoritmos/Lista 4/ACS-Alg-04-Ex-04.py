xant = float(input("Digite a coordenada x de um ponto: "))
yant = float(input("Digite a coordenada y de um ponto: "))
perimetro = 0
x0 = xant
y0 = yant

while True:
    resposta = input("Digite a coordenada x de um ponto (enter para parar): ")
    if resposta == "":
        break
    yatual = float(input("Digite a coordenada y de um ponto: "))
    xatual = float(resposta)
    d = (((xatual - xant) ** 2) + ((yatual - yant) ** 2)) ** 0.5
    perimetro = perimetro + d
    xant = xatual
    yant = yatual

# calcula a distanci do ultimo lado (ultimo ponto até o primeiro ponto)
d = (((x0 - xant) ** 2) + ((y0 - yant) ** 2)) ** 0.5
perimetro = perimetro + d
    

print("O perímetro desse polígono é igual a", perimetro)
