def troca_caractere(string : str):
    string = string[1:]
    string = "0" + string
    return string

word = input("digite uma palavra: ")
palavra = troca_caractere(word)
print(palavra)