# 38. Reserva de assentos

# Crie um sistema de reserva de assentos para um cinema.

# Utilize uma lista com 20 posições.

# Inicialmente, todos os assentos devem estar marcados como:

# "livre"

# O sistema deve permitir:

# Reservar assento;
# Cancelar reserva;
# Mostrar assentos;
# Impedir reserva em assento já ocupado.

assentos = ["Livre"] * 20



def menu():
    print("---------------------------")
    print("Escolha uma opção abaixo:")
    print("1 - Reservar assento")
    print("2 - Cancelar Reserva")
    print("3 - Mostrar assentos")
    print("4 - Sair")
    print("---------------------------")

    opcao = int(input("Digite uma opção: "))

    while opcao < 1 or opcao > 4:
        print("Opção inválida")
        opcao = int(input("Digite uma opção: "))
    
    return opcao

def reservar():
    print(f"Assentos: {assentos}")
    reserva = int(input("Qual assento você quer reservar: "))

    while reserva < 1 or reserva > 20:
        print("Digite um assento válido")
        reserva = int(input("Qual assento você quer reservar: "))

    indice = reserva - 1

    if assentos[indice] == "Ocupado":
        print("Assento já ocupado")
    else:
        assentos[indice] = "Ocupado"
        print("Assento reservado com sucesso")
    
def cancelar():
    print(f"Assentos: {assentos}")
    reserva = int(input("Qual assento você quer cancelar: "))

    while reserva < 1 or reserva > 20 or not reserva:
        print("Digite um assento válido")
        reserva = int(input("Qual assento você quer cancelar: "))

    indice = reserva - 1

    if assentos[indice] == "Livre":
        print("Assento já livre")
    else:
        assentos[indice] = "Livre"
        print("Assento livre com sucesso")


def listar():
    for i in range(len(assentos)):
        print(f"{i+1} - {assentos[i]}")

while True:
    opcao = menu()

    if opcao == 1:
        reservar()
    elif opcao == 2:
        cancelar()
    elif opcao == 3:
        listar()
    else:
        break