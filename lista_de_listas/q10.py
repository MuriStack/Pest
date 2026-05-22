## Exercício 10 - Função para contar pares

# Crie uma função chamada contar_pares.

# A função deve:

# Receber uma lista de números
# Contar quantos números pares existem
# Retornar essa quantidade

# Depois:

# Leia 6 números inteiros
# Armazene os números em uma lista
# Chame a função
# Mostre o resultado

def ler_nums():
    nums = [0, 0, 0, 0, 0, 0]

    for i in range(len(nums)):
        nums[i] = int(input("digite um número: "))
    
    return nums

nums = ler_nums()

def contar_pares(nums : list):
    qtd = 0

    for num in nums:
        if num % 2 == 0:
            qtd += 1
    
    return qtd

qtd = contar_pares(nums)

print(f"A quantidade de números pares na lista é: {qtd}")