## Exercício 1 - Notas de um aluno

# Crie um programa que:

# Leia 4 notas de um aluno
# Armazene as notas em uma lista
# Calcule a média
# Mostre se o aluno ficou aprovado ou reprovado

# Critério:

# Média maior ou igual a 6: aprovado
# Média menor que 6: reprovado

def ler_notas():
    notas = [0, 0, 0, 0]

    for i in range(len(notas)):
        notas[i] = float(input(f"digite a nota {i+1}: "))
    
    return notas

notas = ler_notas()

def calc_media(notas : list):
    acc = 0 

    for nota in notas:
        acc += nota
    
    return acc/len(notas)

media = calc_media(notas)

if media >= 6:
    print(f"Aprovado, sua média foi: {media}")
else: 
    print(f"Reprovado, sua média foi: {media}")
