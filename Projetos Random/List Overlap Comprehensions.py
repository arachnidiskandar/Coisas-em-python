import random
lista_1 = [random.randint(1,20) for i in range(random.randint(1,15))]
lista_2 = [random.randint(1,20) for i in range(random.randint(1,15))]
termos_comum = [termo for termo in lista_1 if termo in lista_2 ]
print(lista_1)
print(lista_2)
print(termos_comum)