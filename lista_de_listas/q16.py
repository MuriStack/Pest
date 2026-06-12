# 16. Palavra em lista

# Leia uma palavra digitada pelo usuário.

# Armazene cada letra dessa palavra em uma lista.

# Ao final, exiba a lista criada.

# Exemplo:

# Entrada: casa

# Saída:
# ['c', 'a', 's', 'a']

palavra = str(input("digite uma palavra: "))

letras = []

for letra in palavra:
    letras.append(letra)

print(f"Letras da palavra digitada: {letras}")
