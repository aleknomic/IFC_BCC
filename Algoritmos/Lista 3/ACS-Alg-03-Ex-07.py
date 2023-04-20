volume = int(input("Digite o nível de decibéis: "))

if volume < 40:
    print("Seu volume está MUITO baixo.")
elif volume == 40:
    print("Seu volume está no nível SALA SILENCIOSA")
elif volume < 70:
    print("Seu volume está entre os níveis SALA SILENCIOSA e DESPERTADOR")
elif volume == 70:
    print("Seu volume está no nível DESPERTADOR")
elif volume < 106:
    print("Seu volume está entre os níveis DESPERTADOR e CORTADOR DE GRAMA")
elif volume == 106:
    print("Seu volume está no nível CORTADOR DE GRAMA")
elif volume < 130:
    print("Seu volume está entre os níveis CORTADOR DE GRAMA e BRITADEIRA")
elif volume == 130:
    print("Seu volume está no nível BRITADEIRA")
else:
    print("Seu volume está MUITO alto.")
    