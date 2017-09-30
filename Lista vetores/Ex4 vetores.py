import random
vetornormal=[]
vetorinvertido=[]
for i in range(10):
    vetornormal.append(random.randint(1,15))
for i in range(9,-1,-1):
    vetorinvertido.append(vetornormal[i])
print("Normal: ",vetornormal)
print("Invertido: ",vetorinvertido)