# 42. Matriz 4x4

# Crie uma matriz 4x4 utilizando listas aninhadas.

# Depois, exiba:

# A matriz completa;
# A soma de cada linha;
# A soma de cada coluna;
# O maior valor da matriz;
# A posição (linha e coluna) onde esse valor foi encontrado.

matriz = []

def completar():
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(int(input(f"Digite o {j+1} da {i+1} linha: ")))
        matriz.append(linha)
    
def mostrar_matriz():
    for linha in matriz:
        print(linha)

def somar_linhas():
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[i][j]
        print(f"Linha {i+1}: {soma}")

def soma_colunas():
    for j in range(len(matriz)):
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][j]
        print(f"Coluna {j+1}: {soma}")

def maior_valor():
    maior = matriz[0][0]
    linha = 0
    coluna = 0

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                linha = i
                coluna = j

    return maior, linha, coluna

completar()

mostrar_matriz()
somar_linhas()
soma_colunas()

maior, linha, coluna = maior_valor()

print(f"Maior valor: {maior}")
print(f"Posição: linha {linha+1}, coluna {coluna+1}")