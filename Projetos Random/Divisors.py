numero = int(input("Digite um número:"))
divisores = []
for i in range(1,numero):
    if numero%i is 0:
        divisores.append(i)

print("Divisores do número {}:".format(numero),divisores)