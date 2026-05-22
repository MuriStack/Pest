## Exercício 2 - Quantidade de aprovados

# Crie um programa que:

# Leia as notas de 6 alunos
# Armazene as notas em uma lista
# Conte quantos alunos tiveram nota maior ou igual a 7

def ler_notas():
    notas = [0, 0, 0, 0, 0, 0]

    for i in range(len(notas)):
        notas[i] = float(input(f"digite a nota {i+1}: "))

    return notas

notas = ler_notas()

qtd = 0

for nota in notas:
    if nota >= 7:
        qtd += 1

print(f"A quantidade de alunos que tiveram nota maior ou igual a 7 foi: {qtd}")