# 39. Carrinho de compras

# Crie um sistema de carrinho de compras.

# Cada item deve ser armazenado no formato:

# [nome, quantidade, preco_unitario]

# O programa deve permitir:

# Adicionar item;
# Remover item;
# Alterar quantidade;
# Calcular valor total da compra.

compras = []

def menu():
    print("-------------------------")
    print("Escolha uma opção abaixo")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Alterar quantidade")
    print("4 - Calcular valor total")
    print("5 - Sair")
    print("-------------------------")

    opcao = int(input("Digite uma opção: "))

    while opcao < 1 or opcao > 5:
        print("Opção inválida")
        opcao = int(input("Digite uma opção: "))

    return opcao

def add_item():
    item = []

    nome = str(input("Digite o nome do item: ")).capitalize()

    while not nome:
        print("Nome não pode estar vázio")
        nome = str(input("Digite o nome do item: ")).capitalize()
    
    quantidade = int(input("Digite a quantidade: "))

    while quantidade <= 0:
        print("Digite uma quantidade válida")
        quantidade = int(input("Digite a quantidade: "))

    preco = float(input("Digite o preço do item: "))

    while preco < 0:
        print("Digite um preço válido")
        preco = float(input("Digite o preço do item: "))

    item.append(nome)
    item.append(quantidade)
    item.append(preco)

    compras.append(item)

    print("Item adicionado com sucesso")

def remover():
    nome = str(input("Digite o nome do item: ")).capitalize()

    while not nome:
        print("Nome não pode estar vázio")
        nome = str(input("Digite o nome do item: "))

    encontrado = False

    if len(compras) > 0:
        for i in range(len(compras)):
            if compras[i][0] == nome:
                compras.pop(i)
                print("Item removido com sucesso")
                encontrado = True
                break
        if not encontrado:
            print("Item não encontrado")
    else:
        print("Compras vázias")

def alterar():
    nome = str(input("Digite o nome do item: ")).capitalize()

    while not nome:
        print("Nome não pode estar vázio")
        nome = str(input("Digite o nome do item: ")).capitalize()

    nova_quantidade = int(input("Digite a nova quantidade"))

    while nova_quantidade <= 0:
        print("Digite uma quantidade válida")
        nova_quantidade = int(input("Digite a nova quantidade"))

    encontrado = False

    if len(compras) > 0:
        for i in range(len(compras)):
            if compras[i][0] == nome:
                compras[i][1] = nova_quantidade
                print("Quantidade alterada")
                encontrado = True
                break
        if not encontrado:
            print("Item não encontrado")
    else:
        print("Compras vázias")

def total():
    acc = 0

    if len(compras) > 0:
        for item in compras:
            acc += item[1] * item[2]
    else:
        print("Compras vázias")

    return acc 

while True:
    opcao = menu()

    if opcao == 1:
        add_item()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        valor = total()
        print(f"Valor total = {valor}")
    else:
        break