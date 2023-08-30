listaneg = []
listazero = []
listapos = []
while True:
    numero = input("Digite um número: ")
    if numero == "":
        break
    n = int(numero)
    if n < 0:
        listaneg.append(n)
    if n > 0:
        listapos.append(n)
    if n == 0:
        listazero.append(n)
print(listaneg)
listafinal = listaneg + listazero + listapos
for i in listafinal:
    print(i)
