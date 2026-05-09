#Leia uma string digitada pelo usuário e informe: Quantas letras ela possui, quantos números ela possui, quantos outros caracteres ela possui.
str = input("digite uma string: ")

qtd_carac = len(str)
letras = 0
nums = 0
outro_carac = 0

for i in range(len(str)):
    if str[i].isdigit():
        nums += 1
    elif str[i].isalpha():
        letras += 1
    else:
        outro_carac += 1

print(f"Caracteres: {qtd_carac}")
print(f"Letras: {letras}")
print(f"Números: {nums}")
print(f"Outros caracteres: {outro_carac}")