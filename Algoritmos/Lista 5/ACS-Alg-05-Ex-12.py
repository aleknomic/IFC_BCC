def main():
    senha = input("Digite a senha: ")
    resultado = verificarsenha(senha)
    if resultado == True:
        print("Sua senha é válida.")
    else:
        print("Sua senha é inválida.")


def verificarsenha(senha):
    numero = False
    maiscula = False
    minuscula = False
    if len(senha) >= 8:
        for i in range(len(senha)):
            i = ord(senha[i])
            if i >= 48 and i < 58:
                numero = True
            if i >= 65 and i < 91:
                maiscula = True
            if i >= 97 and i < 123:
                minuscula = True
    if numero == True and maiscula == True and minuscula == True:
        return True
    else:
        return False


main()
