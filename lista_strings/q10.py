#Crie uma função chamada contar_caracteres que receba uma string como parâmetro e retorne a quantidade de caracteres dessa string sem usar a função len(). Depois, leia uma palavra do usuário, chame a função e mostre o resultado.

def contar_caracteres(string : str):
    qtd = 0
    for caractere in string:
        qtd += 1
    return qtd

string = input("digite uma palavra: ")
print(contar_caracteres(string))