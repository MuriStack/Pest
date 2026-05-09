#Leia o nome completo de uma pessoa e mostre: O nome todo em letras maiúsculas, o nome todo em letras minúsculas, a quantidade total de caracteres, sem contar espaços, a primeira letra do nome.
str = input("digite uma string: ")

str_maiuscula = str.upper()
str_minuscula = str.lower()
qtd_carac = len(str)
primeira_letra = str[0]

print(f"Maiúscula: {str_maiuscula}")
print(f"Minúscula: {str_minuscula}")
print(f"Caracteres: {qtd_carac}")
print(f"Primeira letra: {primeira_letra}")