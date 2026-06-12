nomes = []

for i in range(5):
    nomes.append(str(input(f"digite o {i+1}º nome: ")))

print(f"Lista completa: {nomes}")
print(f"O primeiro nome cadastrado: {nomes[0]}")
print(f"O último nome cadastrado: {nomes[len(nomes) - 1]}")
