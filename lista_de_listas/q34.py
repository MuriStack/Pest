# 34. Removendo negativos

# Leia 10 números inteiros e armazene-os em uma lista.

# Depois, remova todos os números negativos da lista.

# Atenção: ao remover elementos durante uma repetição, a posição dos elementos muda.

nums = []

def ler_nums():
    for i in range(10):
        nums.append(int(input(f"digite o {i+1} número: ")))
    
def remover_negativo(nums : list):
    for i in range(len(nums)-1 , -1, -1):
        if nums[i] < 0:
            nums.pop(i)

ler_nums()

remover_negativo(nums)

print(nums)