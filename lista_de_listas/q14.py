### 14. Média das notas

#Crie um programa que leia 4 notas de um aluno e armazene-as em uma lista.

# Depois, calcule e exiba a média das notas.

notas = []
acc = 0

for i in range(4):
    nota = float(input(f"digite a {i+1}a nota: "))
    acc += nota
    notas.append(nota)

media = acc / len(notas)

print(f"A média foi de: {media}")
