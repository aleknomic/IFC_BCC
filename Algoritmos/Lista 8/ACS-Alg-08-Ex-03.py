def palindromo(frase):
    if len(frase) <= 1:
        return True
    return (frase[0] == frase[-1]) and (palindromo(frase[1:-1]))

def main():
    frase = input("Digite a frase: ")
    f_semespaço = ''.join(frase.split())
    print(palindromo(f_semespaço))

main()