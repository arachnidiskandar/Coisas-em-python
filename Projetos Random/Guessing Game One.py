'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random

def adivinhar():
    numero = random.randint(1, 10)
    ntentativa = 0
    while True:
        tentativa = int(input("Tente adivinhar o número de 1 a 10."))
        if tentativa > numero:
            print("Muito alto.")
            ntentativa += 1
        elif tentativa < numero:
            print("Muito baixo.")
            ntentativa += 1
        else:
            print("Acertou")
            ntentativa += 1
            print("Total de tentativas: {}".format(ntentativa))
            break

while True:
    adivinhar()
    jogar_novamente = input("Se deseja parar, digite 'sair'.")
    if jogar_novamente == 'sair':
        break

