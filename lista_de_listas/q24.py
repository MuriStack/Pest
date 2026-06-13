# 24. Produtos e preços

# Leia vários produtos e seus respectivos preços.

# Armazene os nomes em uma lista e os preços em outra lista.

# Ao final, exiba apenas os produtos cujo preço seja maior que R$ 50,00.

produtos = []
precos = []
maiores_produtos = []

def adicionar_produtos():
    while True:
        produto = str(input("Digite o nome do produto (digite fim para sair): "))
        if produto == "fim":
            break
        else:
            produtos.append(produto)

def adicionar_precos():
    for i in range(len(produtos)):
        precos.append(float(input(f"Digite o preço do {i+1}º produto: ")))

def verificar_preco():
    for i in range(len(produtos)):
        if precos[i] > 50:
            maiores_produtos.append(produtos[i])

adicionar_produtos()
adicionar_precos()
verificar_preco()

print(f"Lista de produtos maiores que R$50,00: {maiores_produtos}")