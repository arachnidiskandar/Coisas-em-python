def comparar(j1, j2):
    if j1 == j2:
        print("Empate")
    else:
        if j1 is 1:
            if j2 is 3:
                print("Parabéns '{}', Você é o vencedor!".format(player1))
            else:
                print("Parabéns '{}', Você é o vencedor!".format(player2))
        elif j1 is 2:
            if j2 is 1:
                print("Parabéns '{}', Você é o vencedor!".format(player1))
            else:
                print("Parabéns '{}', Você é o vencedor!".format(player2))
        elif j1 is 3:
            if j2 is 1:
                print("Parabéns '{}', Você é o vencedor!".format(player2))
            else:
                print("Parabéns '{}', Você é o vencedor!".format(player1))
        else:
            print("Umas das jogadas está incorreta.")

player1 = (input("Nome player 1:"))
player2 = (input("Nome player 2:"))

while True:
    j1 = int(input("Selecione a jogada {}:\n1-Pedra\n2-Papel\n3-Tesoura".format(player1)))
    j2 = int(input("Selecione a jogada {}:\n1-Pedra\n2-Papel\n3-Tesoura".format(player2)))
    comparar(j1, j2)

    jogar_dnv = input('Deseja jogar novamente?("Qalquer Tecla-Sim| N-Não)')
    if jogar_dnv.lower() == "n":
        break


