import random
def jogardado():
    dice=random.randint(1,20)
    return dice

def main():
    rolar=True
    while rolar==True:
        jogardado()
        print("O número jogado é {}".format(jogardado()))
        jogardnv=input("Deseja jogar novamente?(N-Não | Qualquer tecla-Sim)")
        if jogardnv.lower() != "n":
            jogardado()
        else:
            rolar=False

main()
