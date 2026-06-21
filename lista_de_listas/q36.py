# 36. Boletim escolar

# Crie um programa de boletim escolar.

# Cada aluno deve possuir:

# Nome;
# Lista com 3 notas;
# Média;
# Situação.

# A situação deve ser:

# Aprovado (média ≥ 7);
# Recuperação (5 ≤ média < 7);
# Reprovado (média < 5).

# Utilize funções para modularizar o sistema.

alunos = []

def menu():
    print("----------------------------")
    print("Escolha uma opção abaixo:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Listar aluno")
    print("4 - Sair")
    print("----------------------------")

    opcao = int(input("Digite uma opção: "))

    while opcao > 4 or opcao < 1:
        print("Opção inválida")
        opcao = int(input("Digite uma opção: "))
    
    return opcao

def calcular_media(notas : list) -> float:
    acc = 0

    for nota in notas:
        acc += nota

    media = acc / len(notas)

    return media

def add_aluno():
    aluno = []
    notas = []

    nome = str(input("Digite o nome do aluno: ")).capitalize()

    while not nome:
        print("Nome vázio")
        nome = str(input("Digite o nome do aluno: ")).capitalize()

    aluno.append(nome)

    for i in range(3):
        notas.append(float(input(f"Digite a {i+1}º nota: ")))
    
    aluno.append(notas)

    media = calcular_media(notas)

    aluno.append(media)

    if media >= 7:
        aluno.append("Aprovado")
    elif media >= 5:
        aluno.append("Recuperação")
    else:
        aluno.append("Reprovado")

    alunos.append(aluno)

    print(f"{nome} cadastrado com sucesso")

def listar_alunos():
    if len(alunos) > 0:
        for aluno in alunos:
            print(f"Nome: {aluno[0]}")
            print(f"Notas: {aluno[1][0]}, {aluno[1][1]}, {aluno[1][2]}")
            print(f"Média: {aluno[2]}")
            print(f"Situação: {aluno[3]}")
            print("---------------------------------")
    else:
        print("Nenhum aluno cadastrado")

def listar_aluno():
    nome = str(input("Digite o nome do aluno: ")).capitalize()
    encontrado = False

    if len(alunos) > 0:
        for aluno in alunos:
            if aluno[0] == nome:
                print(f"Nome: {aluno[0]}")
                print(f"Notas: {aluno[1][0]}, {aluno[1][1]}, {aluno[1][2]}")
                print(f"Média: {aluno[2]}")
                print(f"Situação: {aluno[3]}")
                print("---------------------------------")
                encontrado = True
        if not encontrado:
            print("Nenhum aluno com esse nome")
    else:
        print("Nenhum aluno cadastrado")

while True:
    opcao = menu()

    if opcao == 1:
        add_aluno()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        listar_aluno()
    else:
        break