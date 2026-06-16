# 30. Removendo repetidos

# Crie uma função chamada:

# remover_repetidos(lista: list) -> list

# A função deve retornar uma nova lista sem elementos repetidos.

# Não utilize set().

lista = []

def ler_elementos(lista : list) -> None:
    while True: 
        elemento = input("digite alguma coisa (digite -1 para parar): ")

        if elemento == '-1':
            break

        lista.append(elemento)

def remover_repetidos(lista : list) -> list:
    nova_lista = []
    
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    
    return nova_lista

ler_elementos(lista)

sem_repetidos = remover_repetidos(lista)

print(f"Lista original: {lista}")

print(f"Lista sem repetidos: {sem_repetidos}")