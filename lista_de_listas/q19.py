# 19. Lista de compras

# Crie um programa para gerenciar uma lista de compras.

# O programa deve permitir:

# - Adicionar item;
# - Remover item;
# - Exibir lista;
# - Encerrar programa.

# Utilize funções próprias para cada operação.

def menu():
    print("----------------------")
    print("0 - Encerrar programa")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Exibir lista")
    print("----------------------")

def adicionar(compras : list):
    item = str(input("digite o item: "))
    compras.append(item)

def remover(compras : list):
    item = str(input("digite o item: "))
    for produto in compras:
        if item == produto:
            compras.remove(produto)
        else:
            print(f"{item} não está na lista")

def exibir(compras : list):
    print(f"Lista de compras: {compras}")

lista = []

while True:
    menu()
    opcao = int(input("digite uma opção: "))
    if opcao == 0:
        print("Programa foi encerrado")
        break
    if opcao == 1:
        adicionar(lista)
    elif opcao == 2:
        remover(lista)
    elif opcao == 3:
        exibir(lista)
    else:
        print("Opção inválida")
