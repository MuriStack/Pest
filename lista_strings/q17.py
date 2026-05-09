#Crie um programa que peça ao usuário para digitar uma senha. Depois, crie uma função chamada validar_senha que receba essa senha e retorne True se ela for válida ou False se for inválida. A senha será considerada válida somente se atender a todas as regras abaixo: Ter pelo menos 8 caracteres, não possuir espaços, possuir pelo menos uma letra maiúscula, possuir pelo menos uma letra minúscula, possuir pelo menos um número
password = input("digite uma senha: ")

def validar_senha(password : str):
    num = False
    minuscula = False
    maiuscula = False
    space = False

    if len(password) < 8:
        return "senha inválida"
    
    for caractere in password:
        if caractere.isspace():
            space = True
        elif caractere.isupper():
            maiuscula = True
        elif caractere.islower():
            minuscula = True
        elif caractere.isdigit():
            num = True
            
    if num and minuscula and maiuscula and not space:
        return "senha válida"
    
    return "senha inválida"

print(validar_senha(password))