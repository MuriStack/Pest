# 23. Fila de atendimento

# Crie um programa que simule uma fila de atendimento.

# O sistema deve permitir:

# - Adicionar uma pessoa ao final da fila;
# - Atender a primeira pessoa da fila usando `pop(0)`;
# - Mostrar a fila atual.

# Utilize funções para organizar o código.

fila = []

def adicionar_pessoa():
    pessoa = str(input("Digite o nome da pessoa: "))
    fila.append(pessoa)
    print(f"{pessoa} foi adicionado(a) ao final da fila")

def atender_pessoa():
    if len(fila) == 0:
        print(f"A fila está vazia")
    else:
        atendida = fila.pop(0)
        print(f"{atendida} foi chamado(a) para atendimento")

def mostrar_fila():
    if len(fila) == 0:
        print(f"Fila atual: [Vazia]")
    else:
        print(f"Fila atual: {fila}")