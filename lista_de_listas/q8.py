## Exercício 8 - Procurando um número

# Crie um programa que:

# Leia 6 números inteiros
# Armazene os números em uma lista
# Depois leia um número de busca
# Informe se esse número aparece ou não na lista

def ler_nums():
    nums = [0, 0, 0, 0, 0, 0]

    for i in range(len(nums)):
        nums[i] = float(input("digite um número: "))
    
    return nums

nums = ler_nums()

num_busca = float(input("digite um número: "))

encontrou = False

for num in nums:
    if num_busca == num:
        encontrou = True

if encontrou:
    print(f"O número {num_busca} aparece na lista")
else:
    print(f"O número {num_busca} não aparece na lista")