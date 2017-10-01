'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of
 this list in it.
'''
import random
lista = [random.randrange(1,50) for i in range(10)]
lista_par = [ i for i in lista if i%2==0 ]
print(lista)
print(lista_par)