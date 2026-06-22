# 37. Agenda de contatos

# Crie um sistema de agenda utilizando listas aninhadas.

# Cada contato deve conter:

# Nome;
# Telefone;
# E-mail.

# O sistema deve permitir:

# Cadastrar;
# Pesquisar;
# Editar;
# Remover contatos.

# Não permita cadastro com nome vazio.

contatos = []

def menu():
    print("------------------------")
    print("Escolha uma opção abaixo")
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Editar")
    print("4 - Remover contatos")
    print("5 - Sair")
    print("------------------------")

    opcao = int(input("Digite uma opção: "))

    while opcao < 1 or   opcao > 5:
        print("Opção inválida")
        opcao = int(input("Digite uma opção: "))

    return opcao

def cadastrar():
    contato = []

    nome = str(input("Digite o nome do contado: ")).capitalize()

    while not nome:
        print("Nome não pode estar vázio")
        nome = str(input("Digite o nome do contado: ")).capitalize()
    
    contato.append(nome)
    
    telefone = str(input("Digite o telefone: "))

    contato.append(telefone)

    email = str(input("Digite o e-mail do contato: "))

    contato.append(email)

    contatos.append(contato)

    print(f"{nome} cadastrado com sucesso")

def pesquisar():
    nome = str(input("Digite o nome do contato: ")).capitalize()
    encontrado = False

    if len(contatos) > 0:
        for contato in contatos:
            if contato[0] == nome:
                print(f"Nome: {contato[0]}")
                print(f"Telefone: {contato[1]}")
                print(f"Email: {contato[2]}")
                encontrado = True
        if not encontrado:
            print("Nenhum contato com esse nome")
    else:
        print("Nenhum contato cadastrado")

def editar():
    nome = str(input("Digite o contato que você quer editar: ")).capitalize()
    encontrado = False

    if len(contatos) > 0:
        for contato in contatos:
            if contato[0] == nome:
                contato[0] = str(input("Digite o novo nome: ")).capitalize()
                while not contato[0]:
                    print("Nome não pode estar vázio")
                    contato[0] = str(input("Digite o novo nome: ")).capitalize()

                contato[1] = str(input("Digite o novo telefone: "))

                contato[2] = str(input("Digite o novo email: "))
                encontrado = True
        if not encontrado:
            print("Nenhum contato com esse nome")
    else:
        print("Nenhum contato cadastrado")

def remover():
    nome = str(input("Digite o nome do contato: ")).capitalize()
    encontrado = False

    if len(contatos) > 0:
        for i in range(len(contatos)):
            if contatos[i][0] == nome:
                contatos.pop(i)
                print("Contato removido com sucesso")
                encontrado = True
                break
        if not encontrado:
            print("Nenhum contato com esse nome")
    else:
        print("Nenhum contato cadastrado")

while True:
    opcao = menu()

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        editar()
    elif opcao == 4:
        remover()
    else:
        print("Encerrado")
        break