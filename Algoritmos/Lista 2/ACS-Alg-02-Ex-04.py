a =int(input("digite o primeiro numero: "))
b =int(input("digite o primeiro numero: "))
c =int(input("digite o primeiro numero: "))

min = min(a, b, c)
max = max(a, b, c)

print("O minimo valor é: ",min)
print("O valor intermediario é: ",(a+b+c)-min-max)
print("O maior valor é: ",max)

