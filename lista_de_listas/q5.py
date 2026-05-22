## Exercício 5 - Temperaturas da semana

# Crie um programa que:

# Leia 7 temperaturas
# Armazene as temperaturas em uma lista
# Calcule a média da semana
# Mostre quantos dias tiveram temperatura acima da média

def ler_temp():
    temperaturas = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(temperaturas)):
        temperaturas[i] = float(input("digite uma temperatura: "))
    
    return temperaturas

temperaturas = ler_temp()

def calc_media_temp(temperaturas : list):
    acc = 0

    for temperatura in temperaturas:
        acc += temperatura
    
    return acc / len(temperaturas)

media_temp = calc_media_temp(temperaturas)

print(f"A média foi de: {media_temp:.2f}")

qtd = 0

for temperatura in temperaturas:
    if temperatura > media_temp:
        qtd += 1

print(f"Tiveram {qtd} dias acima da média")