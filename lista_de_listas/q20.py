# 20. Pesquisa de nomes

# Leia vários nomes e armazene-os em uma lista.

# O cadastro deve terminar quando o usuário digitar fim.

# Depois, peça um nome para pesquisa.

# Informe se o nome está ou não na lista.

nomes = []

while True:
    nome = str(input("Digite um nome (digite fim para sair): "))

    if nome == "fim":
        break

    nomes.append(nome)

pesquisa = str(input("digite um nome de pesquisa: "))

if pesquisa in nomes:
    print(f"O nome {pesquisa} está na lista")
else:
    print(f"O nome {pesquisa} não está na lista")
