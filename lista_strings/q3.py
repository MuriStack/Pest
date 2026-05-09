#Leia uma palavra digitada pelo usuário e mostre uma nova palavra em que o primeiro caractere seja substituído por 0.
str = input("digite uma string: ")
nova_string = "0" + str[1:]
print(nova_string)