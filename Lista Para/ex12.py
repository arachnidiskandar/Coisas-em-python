n1=int(input('Insira o primeiro número:'))
n2=int(input('Insira o segundo número:'))
primo=True
if n1>n2:
    for i in range(2,n2+1):
        if n1%i==0 and n2%i==0:
            primo=False
else:
    for i in range(2,n1+1):
        if n1%i==0 and n2%i==0:
            primo=False
if primo==False:
    print('Não são primos entre si.')
else:
    print('São primos entre si.')