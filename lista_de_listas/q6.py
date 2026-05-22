## Exercício 6 - Estoque baixo

# Crie um programa que:

# Leia a quantidade em estoque de 5 produtos
# Armazene as quantidades em uma lista
# Mostre quantos produtos estão com estoque menor que 10

def qtd_estoque():
    produtos = [0, 0, 0, 0, 0]

    for i in range(len(produtos)):
        produtos[i] = int(input("digite a quantidade de tal produto no estoque: "))

    return produtos

qtd_produtos = qtd_estoque()

menor_10 = 0

for produto in qtd_produtos:
    if produto < 10:
        menor_10 += 1

print(f"A quantidade de produtos que estão com estoque menor que 10 é: {menor_10}")