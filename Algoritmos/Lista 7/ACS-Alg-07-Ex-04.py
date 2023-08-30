d_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def retirarpontos_e_upper(frase):
    frasesempontos = ""
    for i in frase:
        if i == "," or i == "." or i == "!" or i == " " or i == "?":
            continue
        else:
            frasesempontos = frasesempontos + i
    frasefinal = frasesempontos.upper()
    return frasefinal


def traduzir(frase, dicionario):
    frasetraduzida = ""
    for i in frase:
        if (i in dicionario) == True:
            l_morse = dicionario.get(i)
            frasetraduzida = frasetraduzida + " " + l_morse
    return frasetraduzida


def main():
    frase = input("Digite a frase que deseja traduzir: ")
    frase1 = retirarpontos_e_upper(frase)
    print(traduzir(frase1, d_morse))


main()
