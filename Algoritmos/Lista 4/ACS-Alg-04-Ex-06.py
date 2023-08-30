while True:
    grupo = input("Digite o grupo de 8 bits (enter para parar): ")
    if grupo == "":
        break
    if len(grupo) != 8:
        print("ERRO: a palavra precisa ter 8 bits!")
        continue
    if grupo.count("1") + grupo.count("0") != 8:
         print("ERRO: o grupo precisa conter apenas ter 0 ou 1!")
         continue
    if grupo.count("1") % 2 == 0:
          print("O bit de pariedade precisa ser 1")
    else:
            print("O bit de pariedade precisa ser 0")

print("ACABOU")