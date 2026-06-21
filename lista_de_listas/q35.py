# 35. Banco de dados de filmes

# Crie um sistema para armazenar filmes utilizando listas aninhadas.

# Cada filme deve conter:

# Título;
# Diretor;
# Ano;
# Gênero.

# O sistema deve permitir:

# Adicionar filmes;
# Pesquisar por gênero;
# Listar todos os filmes.

# Faça validações para impedir campos vazios.

# Não utilize try e except.

filmes = []

def menu():
    print("1 - Adicionar filme")
    print("2 - Pesquisar por gênero")
    print("3 - Listar todos os filmes")
    print("4 - Sair")
    opcao = int(input("digite uma opção: "))

    while opcao < 1 or opcao > 4:
        print("Opção inválida")
        opcao = int(input("digite uma opção: "))

    return opcao

def add_filme():
    filme = []

    titulo = str(input("digite o título do filme: "))

    while titulo == "":
        print("Título vázio")
        titulo = str(input("digite o título do filme: "))

    filme.append(titulo)

    diretor = str(input("digite o nome do diretor: "))

    while diretor == "":
        print("Nome vazio")
        diretor = str(input("digite o nome do diretor: "))
    
    filme.append(diretor)

    ano = str(input("digite o ano de lançamento: "))

    while ano == "":
        print("Ano vazio")
        ano = str(input("digite o ano de lançamento: "))

    filme.append(ano)

    genero = str(input("digite o gênero do filme: ")).capitalize()

    while genero == "":
        print("Gênero vázio")
        genero = str(input("digite o gênero do filme: ")).capitalize()

    filme.append(genero)

    filmes.append(filme)

def pesquisar_genero():
    genero = str(input("digite o gênero: ")).capitalize()
    saida = []

    for filme in filmes:
        if filme[3] == genero:
            saida.append(filme)
    
    if saida:
        for filme in saida:
            print(f"Título: {filme[0]}")
            print(f"Diretor: {filme[1]}")
            print(f"Ano: {filme[2]}")
            print(f"Gênero: {filme[3]}")
            print("---------------------------------------")
    else:
        print("Nenhum filme encontrado")

def listar_filmes():
    if filmes:
        for filme in filmes:
            print(f"Título: {filme[0]}")
            print(f"Diretor: {filme[1]}")
            print(f"Ano: {filme[2]}")
            print(f"Gênero: {filme[3]}")
            print("---------------------------------------")
    else:
        print("Nenhum filme cadastrado")

while True:
    opcao = menu()

    if opcao == 1:
        add_filme()
    elif opcao == 2:
        pesquisar_genero()
    elif opcao == 3:
        listar_filmes()
    else:
        print("Encerrado")
        break