while True:
    frase = input("Digite a frase ou palavra (enter para parar): ")
    if frase == "":
        break
    frase = ''.join(frase.split())
    n = len(frase)
    palindromo = True
    for i in range(n):
        if frase[i] != frase[n-1-i]:
            palindromo = False
            break
    
    
    if palindromo == True:
        print("Essa frase/palavra é palíndroma.")
    else:
        print("Essa frase/palavra não é palíndroma.")
