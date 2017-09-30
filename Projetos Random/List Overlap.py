'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
1.Randomly generate two lists to test this'''

import random
lista1 = [random.randrange(0,20,1) for i in range(random.randint(1,20))]
lista2 = [random.randrange(0,25,1) for j in range(random.randint(1,30))]
elementoscomum = []
print(lista1)
print(lista2)
for num in lista1:
    if num in lista2:
        elementoscomum.append(num)
print("Elementos em comum:",elementoscomum)
