# 17. Números pares

# Leia 6 números inteiros e armazene-os em uma lista.

# Depois, exiba apenas os números pares presentes na lista.

nums = []

for i in range(6):
    nums.append(int(input(f"digite o {i+1}º número: ")))

pares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)

print(f"Lista com somente os números pares: {pares}")
