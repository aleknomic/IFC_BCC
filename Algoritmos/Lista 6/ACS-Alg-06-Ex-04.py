lista = []
lista2 = []
while True:
    palavra = input("Digite a palavra aqui: ")
    if palavra == "":
        break
    lista.append(palavra)
for i in lista:
    if lista2.count(i) == 0:
        lista2.append(i)
print(lista2)
