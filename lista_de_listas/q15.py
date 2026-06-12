# 15. Exibindo uma lista com função

# Crie uma função chamada:

# mostrar_lista(itens: list) -> None

# A função deve receber uma lista e mostrar cada elemento juntamente com sua posição.

# Exemplo:

# 0 -> João
# 1 -> Maria
# 2 -> Pedro

def mostrar_lista(itens : list) -> None:
    for i in range(len(itens)):
        print(f"{i} -> {itens[i]}")

lista = []

i = "1"

while i != "0":
    nome = str(input("digite o nome de uma pessoa (digite 0 para sair): "))
    i = nome
    if i != "0":
        lista.append(nome)

mostrar_lista(lista)
