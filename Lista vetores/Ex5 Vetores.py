import random
vetor1=[]
vetor2=[]
intercalado=[]
for i in range(10):
    vetor1.append(random.randint(-5,5))
    vetor2.append(random.randint(10,20))
print("Vetor 1: ",vetor1)
print("Vetor 2: ",vetor2)
for i in range(10):
    intercalado.append(vetor1[i])
    intercalado.append(vetor2[i])
print("Vetor Intercalado: ",intercalado)