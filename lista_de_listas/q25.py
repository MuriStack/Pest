# 25. Inserindo em posição específica

# Crie uma lista inicial com alguns nomes.

# Peça ao usuário:

# - Um novo nome;
# - Uma posição.

# Utilize insert() para inserir o nome na posição indicada.

# Antes de inserir, verifique se a posição informada é válida.

nomes = []

def inserir_nomes():
    while True:
        nome = str(input("Digite um nome (digite fim para sair): "))

        if nome.lower() == "fim":
            break
        else:
            nomes.append(nome)

def pedir():
    novo_nome = str(input("Digite um novo nome: "))
    posicao = int(input("digite uma posição: "))

    if posicao < 0 or posicao > len(nomes):
        print(f"Posição inválida")
    else:
        nomes.insert(posicao, novo_nome)

inserir_nomes()
pedir()

print(nomes)