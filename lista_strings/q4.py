#Leia uma palavra digitada pelo usuário e mostre uma nova palavra em que o último caractere seja substituído por #.
str = input("digite uma string: ")

str = str[:len(str)-1]
nova_str = str + "#"

print(nova_str)