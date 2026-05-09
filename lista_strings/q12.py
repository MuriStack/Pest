#Crie uma função chamada eh_palindromo que receba uma palavra e retorne True se ela for um palíndromo ou False caso contrário.
def eh_palindromo(string : str):
    return string == string[::-1]

string = input("digite uma string: ")
print(eh_palindromo(string))