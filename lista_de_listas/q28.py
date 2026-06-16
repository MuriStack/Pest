# 28. Controle de despesas

# Crie um programa de controle de despesas utilizando listas aninhadas.

# Cada despesa deve conter:

# Data;
# Descrição;
# Valor.

# O programa deve permitir:

# Cadastrar despesa;
# Listar despesas;
# Calcular o valor total gasto.

despesas = []

def cadastrar_despesa():
    despesa = []

    data = str(input("digite uma data (formato: MM/DD/YY): "))
    despesa.append(data)

    descricao = str(input("digite uma descrição para a despesa: "))
    despesa.append(descricao)

    valor = float(input("digite o valor da despesa: "))

    while valor < 0:
        print("digite um valor positivo")
        valor = float(input("digite o valor da despesa: "))

    despesa.append(valor)

    return despesa

def listar_despesas(despesas : list):
    for i in despesas:
            print(f"Data: {i[0]}")
            print(f"Descrição: {i[1]}")
            print(f"Valor: R${i[2]}")
            print("--------------------")

def calcular_total(despesas : list):
    contador = 0
    for i in despesas:
         contador += i[2]
    
    print(f"Valor total gasto: {contador}")

despesa = cadastrar_despesa(despesas)

despesas.append(despesa)

listar_despesas(despesas)