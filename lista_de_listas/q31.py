# 31. Controle de estoque

# Crie um programa de controle de estoque.

# Cada produto deve ser armazenado no formato:

# [nome, quantidade, preco]

# O sistema deve permitir:

# Cadastrar produto;
# Atualizar quantidade;
# Remover produto;
# Listar estoque.

# Utilize listas aninhadas.

estoque =[]

def menu():
    print("1 - Cadastrar produto")
    print("2 - Atualizar quantidade")
    print("3 - Remover produto")
    print("4 - Listar estoque")
    print("0 - Sair")
    opcao = int(input("digite alguma opção: "))
    
    return opcao

def cadastrar_produto(estoque : list) -> None:
    produto = []
    
    nome = str(input("digite o nome do produto: "))
    produto.append(nome)

    quantidade = int(input("digite a quantidade do produto: "))
    
    while quantidade < 0:
        print("quantidade inválida")
        quantidade = int(input("digite a quantidade do produto: "))

    produto.append(quantidade)

    preco = float(input("digite o preço do produto: "))
    
    while preco < 0:
        print("preço inválido")
        preco = float(input("digite o preço do produto: "))
    
    produto.append(preco)

    estoque.append(produto)
    print("Produto cadastrado")


def atualizar_quantidade(estoque : list) -> None:
    produto_up = str(input("digite o produto: "))
    nova_qtd = int(input("digite a nova quantidade: "))
    encontrado = False

    for produto in estoque:
        if produto_up == produto[0]:
            produto[1] = nova_qtd
            encontrado = True
            print("quantidade atualizada")
            break

    if not encontrado:
        print("Produto não encontrado")

def remover_produto(estoque : list) -> None:
    produto_rmv = str(input("digite o produto: "))
    encontrado = False

    for produto in estoque:
        if produto[0] == produto_rmv:
            encontrado = True
            estoque.remove(produto)
            break

    if not encontrado:
        print("Produto não encontrado")

def listar_estoque(estoque : list) -> None:

    for produto in estoque:
        print(f"Nome: {produto[0]}, quantidade: {produto[1]}, preço: {produto[2]}")
        print("------------------------------------------------------------------")


while True:
    opcao = menu()

    if opcao == 1:
        cadastrar_produto(estoque)
    elif opcao == 2:
        atualizar_quantidade(estoque)
    elif opcao == 3:
        remover_produto(estoque)
    elif opcao == 4:
        listar_estoque(estoque)
    elif opcao == 0:
        break
    else:
        print("Opção inválida")
