## Exercício 9 - Votação

# Crie um programa que:

# Leia 8 votos
# Cada voto pode ser:
# 1 para candidato A
# 2 para candidato B
# 3 para candidato C
# Armazene os votos em uma lista
# Mostre quantos votos cada candidato recebeu

def ler_votos():
    votos = [0, 0, 0, 0, 0, 0, 0, 0]

    print("Candidato A: 1")
    print("Candidato B: 2")
    print("Candidato C: 3")    

    for i in range(len(votos)):
        votos[i] = int(input("Vote em um candidato: "))

    return votos

votos = ler_votos()

qtd_A = 0
qtd_B = 0
qtd_C = 0

for voto in votos:
    if voto == 1:
        qtd_A += 1
    elif voto == 2:
        qtd_B += 1
    elif voto == 3:
        qtd_C += 1
    else:
        print("Voto inválido")

print(f"O candidato A recebeu: {qtd_A} votos")
print(f"O candidato B recebeu: {qtd_B} votos")
print(f"O candidato C recebeu: {qtd_C} votos")