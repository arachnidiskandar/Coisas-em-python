import random
def create_list():
    list1 = [random.randint(0, 100) for i in range(30)]     #creats a random list
    list.sort(list1)        #organize it in crescent order
    list1 = list(set(list1))  #remove repeated numbers
    return list1
def search(ordered_list, element_to_find):
    start_index = 1
    last_index = len(ordered_list)-1        #lenght of the list
    while True:
        middle_index = (start_index + last_index) // 2  #it must be a integer division
        if middle_index < start_index or middle_index > last_index or middle_index < 0: #eventually, the middle index will be less then start if we dont find the number
            return False    #will break the loop if the number isnt it inside the list

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True     #return True if middle element is the number that we want.
        else:
            if element_to_find > middle_element:    #if the number that we digited is bigger than the middle element
                start_index = middle_index + 1      #the start is middle sucessor, because we know that isnt it the middle.
            else:
                last_index = middle_index - 1       #the antecessor of the middle is the new last element


def main():
    list1 = create_list()
    print(list1)
    numero = int(input("Insira um número para a verificação:"))      #ask a number
    print(search(list1, numero))        #call 'search' and print a boolean value.
if __name__ == '__main__':
    main()