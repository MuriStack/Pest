notas = []
acc = 0

for i in range(4):
    nota = float(input(f"digite a {i+1}a nota: "))
    acc += nota
    notas.append(nota)

media = acc / len(notas)

print(f"A média foi de: {media}")
