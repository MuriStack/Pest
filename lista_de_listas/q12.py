### 12. Lista de números

# Crie um programa que peça ao usuário vários números inteiros.

# O programa deve parar quando o usuário digitar `0`.

# Ao final, exiba a lista com todos os números digitados, sem incluir o `0`.

num = 1
nums = []

while num != 0:
    num = int(input("digite um número (digite 0 para sair): "))
  
    if num != 0:
        nums.append(num)
    
print(f"Lista completa dos números digitados: {nums}")
