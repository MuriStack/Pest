def verifica_vogal(string : str):
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "A" or string[i] == "e" or string[i] == "E" or string[i] == "i" or string[i] == "I" or string[i] == "o" or string[i] == "O" or string[i] == "u" or string[i] == "U":
            return True
    return False

def conta_vogal(string : str):
    contador = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "A" or string[i] == "e" or string[i] == "E" or string[i] == "i" or string[i] == "I" or string[i] == "o" or string[i] == "O" or string[i] == "u" or string[i] == "U":
            contador += 1
    return contador

string = input("digite uma string: ")

qtd = conta_vogal(string)

if verifica_vogal(string) == True:
    print("Tem vogal na minha string")
else:
    print("Não tem vogal na minha string")

if qtd > 0:
    print(f"Tem {qtd} vogais na minha string")
else:
    print("Tem 0 vogais na minha string")