# Crie um programa para verificar se um aluno passou de média ou não. Seu programa deve fazer o seguinte:
# - Ler 5 notas de um aluno (usuário/input) e armazená-las em uma lista
# - Seu programa deve calcular a Média Parcial (MP) desse aluno (utilize uma função "calc_media" para calcular a média)
# - Caso a média seja superior a 6 informe que o aluno está aprovado. Caso a média seja inferior a 3 informe que o aluno está reprovado. Caso contrário, leia uma nova nota (Prova Final - PF) usuário e calcule a média final:
# Média Final (MF) = (MP + PF)/2
# - Caso a média final seja inferior a 5, informe que o aluno está reprovado. Caso contrário, informe que o aluno está aprovado.

def ler_notas():
    notas = [0, 0, 0, 0, 0]

    for i in range(len(notas)):
        notas[i] = float(input(f"digite a nota {i+1}: "))
    return notas

def calc_media(l : list):
    acc = 0

    for item in l:
        acc += item

    return acc/len(l)

notas = ler_notas()

media_parcial = calc_media(notas)

if media_parcial >= 6:
    print("Aprovado")
elif media_parcial < 3:
    print("Reprovado")
else:
    print("Recuperação")

    prova_final = float(input("digite a nota da prova final: "))

    def media_final(mp : float, pf : float):
        return (mp + pf)/2
    
    mf = media_final(media_parcial,prova_final)

    if mf < 5:
        print("Reprovado")
    else:
        print("Aprovado")