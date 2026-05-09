#Crie uma função chamada concatenar_fatiar que receba duas strings como entrada: Os três primeiros caracteres da primeira string, os três últimos caracteres da segunda string.
def concatenar_fatiar(string1 : str, string2 : str):
    nova_string = string1[:3] + string2[-3:]
    return nova_string

string1 = input("digite uma string: ")
string2 = input("digite outra string: ")

print(concatenar_fatiar(string1,string2))