# 40. Análise de temperaturas

# Leia as temperaturas dos 7 dias de uma semana.

# Utilizando funções próprias, exiba:

# A maior temperatura;
# A menor temperatura;
# A média da semana;
# Os dias cuja temperatura ficou acima da média.

# Não utilize max() nem min().

temperaturas = []

for i in range(7):
    temperaturas.append(float(input(f"Digite a {i+1}º temperatura: ")))

def maior():
    maior = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura > maior:
            maior = temperatura

    return maior

def menor():
    menor = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura < menor:
            menor = temperatura

    return menor

def media():
    acc = 0

    for temperatura in temperaturas:
        acc += temperatura

    media = acc / len(temperaturas)

    return media

def acima():
    dias = []
    media_semana = media()

    for i in range(len(temperaturas)):
        if temperaturas[i] > media_semana:
            dias.append(f"Dia {i+1}")

    return dias

print(f"Maior temperatura: {maior()}")
print(f"Menor temperatura: {menor()}")
print(f"Média das temperaturas: {media()}")
print(f"Dias acima da média: {acima()}")