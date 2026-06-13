# 26. Maior valor da lista

# Crie uma função chamada:

# maior_valor(numeros: list) -> int

# A função deve retornar o maior valor da lista.

# Não utilize max().

nums = []

def inserir_numeros():
    while True:
        num = int(input("Digite um número (digite 0 para sair): "))
        
        if num == 0:
            break
        else:
            nums.append(num)

def maior_valor(nums : list) -> int:
    maior = nums[0]

    for num in nums:
        if num > maior:
            maior = num
    return maior
    
inserir_numeros()

if len(nums) == 0:
    print("Lista vazia")
else:
    maior = maior_valor(nums)
    print(f"O maior valor é {maior}, da lista {nums}")