# 41. Biblioteca

# Crie um sistema de biblioteca utilizando listas aninhadas.

# Cada livro deve conter:

# Título;
# Autor;
# Ano;
# Situação ("disponível" ou "emprestado").

# O sistema deve permitir:

# Cadastrar livro;
# Emprestar livro;
# Devolver livro;
# Pesquisar livro;
# Listar livros.

livros = []

def menu():
    print("-----------------------")
    print("Digite uma opção abaixo:")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Pesquisar")
    print("5 - Listar livros")
    print("6 - Sair")
    print("-----------------------")

    opcao = int(input("Digite uma opção: "))

    while opcao < 1 or opcao > 6:
        print("Digite uma opção válida")
        opcao = int(input("Digite uma opção: "))

    return opcao

def cadastrar():
    livro = []

    titulo = str(input("Digite o título do livro: ")).capitalize()

    while not titulo:
        print("Não pode título vázio")
        titulo = str(input("Digite o título do livro: ")).capitalize()

    livro.append(titulo)

    autor = str(input("Digite o autor do livro: ")).capitalize()

    while not autor:
        print("Nome do autor está vázio")
        autor = str(input("Digite o autor do livro: ")).capitalize()

    livro.append(autor)

    ano = int(input("Digite o ano do livro: "))

    while ano < 0:
        print("Não digite números negativos")
        ano = int(input("Digite o ano do livro: "))

    livro.append(ano)

    situacao = str(input("Digite a situação do livro (Disponível ou Emprestado): ")).capitalize()

    while situacao != "Disponível" and situacao != "Emprestado":
        print("Situação inválida")
        situacao = str(input("Digite a situação do livro (Disponível ou Emprestado): ")).capitalize()

    livro.append(situacao)

    livros.append(livro)

    print("Livro cadastrado com sucesso")

def emprestar():
    situacao = "Emprestado"
    encontrado = False

    titulo = str(input("Digite o título do livro: ")).capitalize()

    if len(livros) > 0:
        for livro in livros:
            if livro[0] == titulo:
                if not livro[3] == situacao:
                    livro[3] = situacao
                    encontrado = True
                    print("Livro emprestado")
                    break
                else:
                    print("Livro já emprestado")
                    encontrado = True
        if not encontrado:
            print("Livro não encontrado")
    else:
        print("Lista de livros vázia")

def devolver():
    situacao = "Disponível"
    encontrado = False

    titulo = str(input("Digite o título do livro: ")).capitalize()

    if len(livros) > 0:
        for livro in livros:
            if livro[0] == titulo:
                if not livro[3] == situacao:
                    livro[3] = situacao
                    encontrado = True
                    print("Livro disponível")
                    break
                else:
                    print("Livro já disponível")
                    encontrado = True
        if not encontrado:
            print("Livro não encontrado")
    else:
        print("Lista de livros vázia")

def pesquisar():
    titulo = str(input("Digite o título do livro: ")).capitalize()
    encontrado = False

    if len(livros) > 0:
        for livro in livros:
            if livro[0] == titulo:
                print(f"Livro encontrado: {livro}")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado")
    else:
        print("Lista de livros vázia")

def listar():
    if len(livros) > 0:
        for livro in livros:
            print(f"Título: {livro[0]}")
            print(f"Autor: {livro[1]}")
            print(f"Ano: {livro[2]}")
            print(f"Situação: {livro[3]}")
            print("--------------------")
    else:
        print("Lista de livros vázia")

while True:
    opcao = menu()

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        emprestar()
    elif opcao == 3:
        devolver()
    elif opcao == 4:
        pesquisar()
    elif opcao == 5:
        listar()
    else:
        print("Encerrado")
        break