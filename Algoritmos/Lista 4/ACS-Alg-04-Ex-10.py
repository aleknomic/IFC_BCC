while True:
    palavra = input("Digite a palavra (enter para parar): ")
    if palavra == "":
        break
    n = len(palavra)
    palindromo = True
    for i in range(n):
        if palavra[i] != palavra[n-1-i]:
            palindromo = False
            break
    
    
    if palindromo == True:
        print("Essa palavra é palíndroma.")
    else:
        print("Essa palavra não é palíndroma.")