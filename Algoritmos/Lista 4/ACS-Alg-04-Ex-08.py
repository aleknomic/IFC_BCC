msg1 = input("Digite aqui a frase que deseja codificar: ")
distancia = int(input("Digite a distância de deslocamento das letras: "))
msg2 = ""

for letra in msg1: #para cada letra no texto
    if letra == " ": #se for um espaço
        msg2 = msg2 + " " #adiciona um espça na msg criptografada
        continue  # verifca p todos
    codigo = ord(letra) #retorna um número inteiro que representa a letra/caracter
    nova_letra = codigo + distancia #adiciona o valor da letra + valor da distância em uma variavel
    if nova_letra > 90 and nova_letra <= 96:
        nova_letra = nova_letra - 26 #adiciona mais 26 na variavel para voltar para as primeiras letras
    if nova_letra >= 123 and nova_letra <= 127:
        nova_letra = nova_letra - 26
    nova_letra = chr(nova_letra) #volta o valor para um caracter
    msg2 = msg2 + nova_letra #adiciona o caracter na mensagem final

print(msg2) #printa a mensagem final
