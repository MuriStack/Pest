# 27. Inserção ordenada

# Crie um programa que leia vários números inteiros.

# Cada número deve ser inserido na posição correta da lista utilizando `insert()`.

# Ao final, a lista deve estar ordenada em ordem crescente.

# Não utilize:

# - sort()
# - sorted()

nums = []

def ler_nums():
    while True:
        num = int(input("digite um número (digite 0 para sair): "))
        inserido = False
        
        if num == 0:
            break
        else:
            if len(nums) > 0:
                for i in range(len(nums)):
                    if nums[i] > num:
                        nums.insert(i,num)
                        inserido = True
                        break
                if not inserido:
                    nums.append(num)
            else:
                nums.append(num)
    return nums

nums = ler_nums()

print(nums)