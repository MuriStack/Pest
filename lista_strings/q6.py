#Leia uma frase digitada pelo usuário e conte quantas vogais ela possui. O programa deve funcionar mesmo se o usuário digitar letras maiúsculas.
str = input("digite uma string: ")
str = str.lower()

res = 0

for i in range (len(str)):
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        res += 1

print(f"Existe {res} vogais na string")