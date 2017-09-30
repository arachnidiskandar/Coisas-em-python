import random
numeros=[]
positovos=[]
negativos=[]
for i in range(10):
    numeros.append(random.randint(-10,10))
print(numeros)
for i in range(10):
    if numeros[i]<0:
        negativos.append(numeros[i])
    else:
        positovos.append(numeros[i])
print("Positivos: ",positovos)
print("Negativos: ",negativos)