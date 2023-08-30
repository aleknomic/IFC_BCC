import random

def main():
    x = random.randint(7,12)
    senha = ""
    senhafinal = criarsenha(x, senha)
    print("Senha aleatória gerada:", senhafinal)

def criarsenha(x, senha):
    for numero in range(x):
        caracter_ascii = random.randint(33,126)
        caracter = chr(caracter_ascii)
        senha = senha + caracter
    return senha

main()