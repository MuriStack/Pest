# 33. Busca de produtos

# Crie uma função chamada:

# buscar_produto(estoque: list, nome: str) -> int

# A função deve retornar:

# A posição do produto, caso exista;
# -1, caso não exista.

estoque = [
    ["Arroz", 10, 25.90],
    ["Feijão", 5, 8.50],
    ["Macarrão", 20, 4.99],
    ["Açúcar", 8, 6.75],
    ["Café", 12, 15.50]
]

def buscar_produto(estoque : list, nome : str) -> int:
    for i in range(len(estoque)):
        if estoque[i][0] == nome:
            return i
    
    return -1
    
produto = str(input("digite o produto: "))

posicao = buscar_produto(estoque, produto)

print(f"Posição do produto: {posicao}")