import random
vetor=[]
for i in range(10):
    vetor.append(random.randint(1,20))
print(vetor)
for i in range(10):
    if i%2==0:
        vetor[i]=vetor[i]*2
    else:
        vetor[i]=vetor[i]*3
print(vetor)