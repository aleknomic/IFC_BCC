def tokenizacao(expressao):
    lista=[]
    anterior=""
    numero=""
    for elemento in expressao:
        if((elemento =="(") or (elemento==")") or( elemento =="*") or (elemento=="/") or (elemento =="^"))    or   ((elemento=="+" or elemento=="-") and (anterior.isnumeric() or anterior==")")):
            
            if numero != "":
                lista.append(numero)
                numero=""
            lista.append(elemento)
        else:
            numero+=elemento
        anterior=elemento
    if numero != "":
        lista.append(numero)
        numero=""
    return lista

def infix_para_posfix(infix):
    operadores=[]
    postfix=[]
    precedenciaToken=""
    for token in infix:
        if  token[0:].isdigit() or (token[0] == "-" and token[1:].isdigit()):
            postfix.append(token)
        if (token =="*") or (token=="/") or (token =="^") or (token=="+") or (token =="-"):
            while len(operadores)>=1 and operadores[-1] != "(" and precedenciaToken < operadores[-2]:
                postfix.append(operadores[-1])
                operadores.remove(-1)
            operadores.append(token)
        if token =="(":
            operadores.append(token) 
        if token ==")":
            while operadores[-1] != "(":
                postfix.append(operadores[-1])
                operadores.remove(operadores[-1])
            operadores.remove("(")
        precedenciaToken=token
    while len(operadores)>=1:
        postfix.append(operadores[-1])
        operadores.remove(operadores[-1])
        
    return postfix

def avaliar_posfix(listaPosfix):  
    valores=[]
    resposta=""
    for token in listaPosfix:
        if token.isnumeric():
            valores.append(int(token))
        else:
            direita = valores.pop()
            esquerda = valores.pop()
            if token == '-':
                resposta = esquerda - direita
            elif token == '+':
                resposta = esquerda + direita
            elif token == '/':
                resposta = esquerda / direita
            elif token == '*':
                resposta = esquerda * direita
            else:
                return "ERRO: operador inválido"
            valores.append(resposta)
    return(valores)

def main():
    n=input("Digite uma expressão matemática: ")
    infix=tokenizacao(n)
    print(avaliar_posfix(infix_para_posfix(infix)))

main()