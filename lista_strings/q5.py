#Leia uma palavra digitada pelo usuário e mostre apenas os caracteres que estão em posições pares.
str = input("digite uma string: ")

for i in range (len(str)):
    if i % 2 == 0:
        print(str[i])