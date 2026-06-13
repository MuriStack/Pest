# 21. Contando ocorrências

# Crie uma função chamada:

# contar_ocorrencias(lista: list, valor: str) -> int

# A função deve retornar quantas vezes um determinado valor aparece na lista.

# Não utilize count().

def contar_ocorrencias(lista : list, valor : str) -> int:
    acc = 0
    for item in lista:
        if valor == item:
            acc += 1
    return acc