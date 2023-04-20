numero = int(input("Digite um número inteiro de 4 dígitos: "))

d1 = (numero) % 10
d2 = ((numero) // 10) % 10
d3 = ((numero) // 100) % 10
d4 = ((numero) // 1000) % 10

soma = d1 + d2 + d3 + d4

print("A soma dos dígitos do número", numero, "é", (soma))


