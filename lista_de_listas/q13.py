### 3. Removendo frutas

# Crie uma lista contendo 5 frutas.

# Peça ao usuário o nome de uma fruta.

# Se a fruta estiver na lista, remova-a utilizando `remove()`.

# Caso contrário, exiba uma mensagem informando que a fruta não foi encontrada.

fruits = []

for i in range(5):
    fruits.append(str(input(f"digite o nome da {i+1}a fruta: ")))

remover = str(input("digite o nome de alguma fruta: "))

if remover in fruits:
    fruits.remove(remover)
    print(f"A fruta {remover} foi removida")
else:
    print(f"A fruta {remover} não foi encontrada")
