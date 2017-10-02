import random

def remover_duplicados(a):
    a = set(a)
    return list(a)

lista = [random.randint(1, 5) for i in range(8)]
print(lista)
print("Lista sem elementos repitidos: ", remover_duplicados(lista))