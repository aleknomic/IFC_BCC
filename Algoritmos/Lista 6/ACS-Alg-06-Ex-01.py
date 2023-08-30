lista = []
while True:
    numero = int(input("Digite um número (digite 0 para parar): "))
    if numero == 0:
        break
    lista.append(numero)
print(sorted(lista))
