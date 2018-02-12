'''Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a directory if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:

the username is not unique
the age is not a positive integer
the user is under 16
the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)

Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.

Think about where else it would be a good idea to use a custom class, and what kind of collection type would be most appropriate for your directory.

You can consider an email address to be valid if it contains one @ symbol and has a non-empty username and domain name – you don’t need to check for valid characters. You can assume that the age is already an integer value.'''

#Exceções.
class UsernotUnique(Exception):
    pass
class NotPositiveInteger(Exception):
    pass
class Userunder16(Exception):
    pass
class Notvalidemail(Exception):
    pass

#Objeto usuário.
class User(object):
    def __init__(self, theNickname, theEmail):
        self.nickname = theNickname
        self.email = theEmail
    def getNome(self):
        return self.nickname
    def getEmail(self):
        return self.email
    def __str__(self):
        return "nick: {}       email: {}".format(self.getNome(), self.getEmail())

def createUser(qntd):       #Retorna uma lista de tuples com os dados dos usuários.
    import random
    chars = "abcdefghijklmnopqrstuvxywz0123456789"
    users_list = []
    while True:
        if len(users_list) < qntd:       #Loop Para quando a qntd de users for a mesma q o argumento.
            nickname = ""
            email = ""
            age = random.randint(13, 30)
            for i in range(12):
                nickname += random.choice(chars)
            email = nickname+"@gmail.com"
            user = nickname, email, age
            users_list.append(user)
        else:
            break
    return users_list

def main():
    user_list = createUser(10)
    directory = {}
    for nick, email, age in user_list:
        try:
            if nick in directory:
                raise UsernotUnique()
            email_parts = email.split('@')
            if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
                raise Notvalidemail()
            if age < 16:
                raise Userunder16
            if age < 0:
                raise NotPositiveInteger
            else:
                directory[nick] = User(nick, email)
        except UsernotUnique:
            print("Usuário indisponível.")
        except NotPositiveInteger:
            print("Idade inválida.")
        except Userunder16:
            print("Menor de idade.")
        except Notvalidemail:
            print("Email inválido.")
    print(directory)


if __name__ == '__main__':
    main()