## Exercício 7 - Números pares

# Crie um programa que:

# Leia 8 números inteiros
# Armazene os números em uma lista
# Mostre quantos números pares existem na lista

def ler_nums():
    nums = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(nums)):
        nums[i] = float(input("digite um número: "))

    return nums

nums = ler_nums()

qtd = 0

for num in nums:
    if num % 2 == 0:
        qtd += 1

print(f"A quantidade de números de números pares na lista é: {qtd}")