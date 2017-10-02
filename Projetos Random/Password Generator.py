import random
def gerador_senha(tamanho):
   c = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
   senha = "".join(random.sample(c, tamanho))
   return senha

tamanho = int(input("Qntd de caracteres da senha:"))
print("Sua senha é: ", gerador_senha(tamanho))





