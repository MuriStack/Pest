#Leia uma palavra digitada pelo usuário e mostre seus caracteres do último até o primeiro.
str = input("digite uma string: ")
nova_str = str[::-1]

for i in range(len(nova_str)):
    print(nova_str[i])