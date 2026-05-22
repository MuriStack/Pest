# Desafio

## Controle de notas de uma turma

# Crie um programa que:

# Leia as notas de 10 alunos
# Armazene as notas em uma lista
# Calcule a média da turma usando uma função
# Mostre:
# A média da turma
# Quantos alunos ficaram acima da média
# Quantos alunos ficaram abaixo da média
# A maior nota
# A menor nota

# Use apenas:

# Listas com tamanho definido
# Índices
# For
# While
# If, elif, else
# Funções
# Variáveis auxiliares

def ler_notas():
    notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(notas)):
        notas[i] = float(input(f"digite a nota {i+1}: "))
    
    return notas

notas = ler_notas()

def calc_media(notas : list):
    acc = 0

    for nota in notas:
        acc += nota
    
    return acc / len(notas)

media_turma = calc_media(notas)

acima_media = 0
abaixo_media = 0

for nota in notas:
    if nota >= media_turma:
        acima_media += 1
    else:
        abaixo_media += 1

print(f"{acima_media} alunos ficaram com a nota maior que a média da turma")

print(f"{abaixo_media} alunos ficaram com a nota menor que a média da turma")

maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

print(f"A menor nota foi: {menor_nota}")

print(f"A maior nota foi: {maior_nota}")