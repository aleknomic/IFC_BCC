print("Número\tx1\tx2\tx3\tx4\tx5\tx6\tx7\tx8\tx9\tx10")
for i in range (1,11):
    print(i,"\t",i*1,"\t",i*2,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10)

print("Número\tx1\tx2\tx3\tx4\tx5\tx6\tx7\tx8\tx9\tx10")
print("-----------------------------------------------------------------------------------")
for linha in range(1, 11):
    print(linha, end="\t|")
    for coluna in range(1,11):
        print(linha*coluna, end="\t")
    print()

