#Crie uma função chamada inverter_texto que receba uma string como parâmetro e retorne essa string invertida.
def inverter_texto(string : str):
    string_invertida = string[::-1]
    return string_invertida

string = input("digite uma string: ")

print(inverter_texto(string))