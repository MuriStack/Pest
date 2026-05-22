## Exercício 3 - Maior número

# Crie um programa que:

# Leia 5 números inteiros
# Armazene os números em uma lista
# Mostre o maior número da lista

def ler_nums():
    nums = [0, 0, 0, 0, 0]

    for i in range(len(nums)):
        nums[i] = float(input("digite um número: "))

    return nums

nums = ler_nums()

maior = nums[0]

for num in nums:
    if num > maior:
        maior = num

print(f"O maior número da lista é: {maior}")