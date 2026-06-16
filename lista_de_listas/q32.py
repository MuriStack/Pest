# 32. Matriz 3x3

# Crie uma matriz 3x3 utilizando listas aninhadas.

# Depois, exiba:

# A matriz completa;
# A soma de todos os elementos;
# Os elementos da diagonal principal.

matriz = []

def ler_matriz(matriz : list) -> None:
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(int(input(f"digite o {j+1}º número: ")))
        
        matriz.append(linha)

def somar_elementos(matriz : list) -> int | float:
    contador = 0

    for linha in matriz:
        for elemento in linha:
            contador += elemento

    return contador

def diagonal_principal(matriz : list) -> list:
    diagonal = []

    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])

    return diagonal

def exibicao(matriz : list):
    print(f"Matriz completa: {matriz}")

    soma = somar_elementos(matriz)

    print(f"Soma dos elementos: {soma}")

    diagonal = diagonal_principal(matriz)

    print(f"Diagonal principal: {diagonal}")

ler_matriz(matriz)

exibicao(matriz)