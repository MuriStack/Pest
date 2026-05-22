notas = [10, 6, 8, 4, 7.5, 2]

acumulador = 0

for i in notas:
    acumulador += i

media = acumulador/len(notas)

print(media)