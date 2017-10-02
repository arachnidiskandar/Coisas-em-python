def checar_primo(n1):
    i = 2
    primo = True
    while i < n1:
        if n1 % i == 0:
            primo = False
        i += 1


    if primo is True:
        print("O número {} é primo.".format(n1))
    else:
        print("O número {} não é primo.".format(n1))

numero = int(input("Digite um número:"))
checar_primo(numero)