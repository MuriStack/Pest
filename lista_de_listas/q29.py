# 29. Cadastro de alunos

# Crie um sistema de cadastro de alunos utilizando listas aninhadas.

# Cada aluno deve possuir:

# Nome;
# Nota 1;
# Nota 2;
# Média.

# Ao final, exiba todos os alunos e informe quais foram aprovados (média ≥ 7).

alunos = []

def cadastrar_aluno():
        aluno = []

        nome = str(input("digite o nome do aluno: "))
        aluno.append(nome)

        n1 = float(input("digite a primeira nota do aluno: "))

        while n1 < 0:
            print("digite um valor positivo")
            n1 = float(input("digite a primeira nota do aluno: "))
        
        aluno.append(n1)

        n2 = float(input("digite a segunda nota do aluno: "))

        while n2 < 0:
            print("digite um valor positivo")
            n2 = float(input("digite a segunda nota do aluno: "))

        aluno.append(n2)

        media = (n1+n2)/2

        aluno.append(media)

        return aluno

while True:
    aluno = cadastrar_aluno()
    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")

    if continuar.lower() == "n":
        break


aprovados = []

for aluno in alunos:
    if aluno[3] >= 7:
        aprovados.append(aluno[0])

print(f"Alunos aprovados: {aprovados}")