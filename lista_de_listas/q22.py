# 12. Separando pares e ímpares

# Leia 8 números inteiros e armazene-os em uma lista.

# Depois, crie duas novas listas:

# - Uma contendo apenas os números pares;
# - Outra contendo apenas os números ímpares.

# Exiba as três listas.

nums = []

for i in range(8):
    nums.append(int(input(f"digite o {i+1}º número")))

pares = []
impares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista dos números inteiros: {nums}")
print(f"Lista dos números pares: {pares}")
print(f"Lista dos números ímpares: {impares}")