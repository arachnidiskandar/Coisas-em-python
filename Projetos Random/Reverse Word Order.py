def inverter_string(frase):
    return " ".join(frase.split()[::-1])

frase = input("Digite uma frase:")
print("Frase invertida: ", inverter_string(frase))



