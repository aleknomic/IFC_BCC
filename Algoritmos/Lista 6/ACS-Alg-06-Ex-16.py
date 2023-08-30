def precedencia(operador):
    if operador =="+" or operador=="-":
        return 1
    elif operador =="*" or operador=="/":
        return 2
    elif operador =="^":
        return 3
    else:
        return -1

def infix_para_posfix(infix):
    operadores=[]
    postfix=[]
    precedenciaToken=""
    for token in infix:
        if  token[0:].isdigit() or (token[0] == "-" and token[1:].isdigit()) or (token[0] == "+" and token[1:].isdigit()):
            postfix.append(token) 
        if (token =="*") or (token=="/") or (token =="^") or (token=="+") or (token =="-"):
            while len(operadores)>0 and operadores[-1] != "(" and precedencia(token) < precedencia(operadores[-1]):
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
        
    while len(operadores)>=1:
        postfix.append(operadores[-1])
        operadores.remove(operadores[-1])
        
    return postfix
    
def tokenizacao(n):
    lista=[]
    anterior=""
    numero=""
    for elemento in n:
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

def main():
    n=input("Digite uma expressão matemática: ")
    infix=tokenizacao(n)
    print(infix_para_posfix(infix))

main()