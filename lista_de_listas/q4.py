## Exercício 4 - Maior número e posição

# Crie um programa que:

# Leia 5 números inteiros
# Armazene os números em uma lista
# Mostre:
# O maior número
# O índice onde ele está

def ler_nums():
    nums = [0, 0, 0, 0, 0]

    for i in range(len(nums)):
        nums[i] = int(input("digite um número: "))
    
    return nums

nums = ler_nums()

maior = nums[0]
indice = 0

for i in range(len(nums)):
    if nums[i] > maior:
        maior = nums[i]
        indice = i

print(f"O maior número da lista é: {maior} e o seu índice é: {indice}")