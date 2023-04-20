centavos = int(input("Digite a quantidade de centavos: "))

cinquenta = centavos // 50
r_1 = centavos % 50

v_c = r_1 // 25
r_2 = r_1 % 25

dez = r_2 // 10
r_3 = r_2 % 10

cinco = r_3 // 5
uno = r_3 % 5

print("O troco deve ser composto por \n", cinquenta, "moedas de 50 centavos \n", v_c, "moedas de 25 centavos \n", dez, "moedas de 10 centavos \n", cinco, "moedas de 5 centavos \n", uno, "moedas de 1 centavo.")