pi = 3
n = 2
sinal = 1

for i in range(15):
    print(pi)
    pi = pi + (sinal*(4/(n*(n+1)*(n+2))))
    sinal = -sinal
    n = n + 2