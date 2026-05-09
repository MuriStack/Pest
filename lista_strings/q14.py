#Crie um programa que leia o nome e o sobrenome de uma pessoa. Depois, crie uma função chamada gerar_usuario que retorne um nome de usuário formado por: As três primeiras letras do nome, as três últimas letras do sobrenome, tudo em letras minúsculas.
nome = input("digite o seu nome: ")
sobrenome = input("digite o seu sobrenome: ")

def gerar_usuario(nome : str, sobrenome : str):
    nome_usuario = (nome[:3] + sobrenome[-3:]).lower()
    
    return nome_usuario

print(gerar_usuario(nome, sobrenome))    