menorq = int(input("Insira um valor para ser o limite:"))
valores = [2,3,5,7,11,13,17,19,23,29,55,97,44,111]
valoresmenorqnumero = []
for i in valores:
    if i < menorq:
        valoresmenorqnumero.append(i)

print("Os valores da lista menores que {} são:".format(menorq), valoresmenorqnumero)

