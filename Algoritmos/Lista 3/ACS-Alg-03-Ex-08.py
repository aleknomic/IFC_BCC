nome = input("Digite o nome da nota: ")
oitava = int(input("Digite o valor da oitava: "))

if nome == ("c"):
    freq = 261.63
elif nome == ("d"):
    freq = 293.66
elif nome == ("e"):
    freq = 329.63
elif nome == ("f"):
    freq = 349.23
elif nome == ("g"):
    freq = 392.00
elif nome == ("a"):
    freq = 440.00
elif nome == ("b"):
    freq = 493.88

freq_final = freq / (2**(4-oitava))
print("A frequência dessa nota é {:.2f} Hz.".format(freq_final)) 
