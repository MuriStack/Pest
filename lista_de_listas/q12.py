num = 1
nums = []

while num != 0:
    num = int(input("digite um número (digite 0 para sair): "))
  
    if num != 0:
        nums.append(num)
    
print(f"Lista completa dos números digitados: {nums}")
