
'''Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
to largest) and another number. The function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.'''
import random
def create_list():
    list1 = [random.randint(0, 100) for i in range(30)]     #creats a random list
    list.sort(list1)        #organize it in crescent order
    list1 = list(set(list1))      #remove repeated numbers

    return list1
def search_number():
    list1 = create_list()
    print(list1)
    numero = int(input("Digite um número:"))        #Ask a number
    contido = False         #Boolean for verify
    for i in list1:
        if numero == i:     #verify if the number is in the list
            contido = True
    print(contido)
    return contido          #return a boolean

if __name__ == '__main__':
    search_number()


