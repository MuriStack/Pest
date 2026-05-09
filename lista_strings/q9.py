#Crie uma função chamada saudar que receba o nome de uma pessoa como parâmetro e mostre uma mensagem de boas-vindas.

def saudar(nome : str):
    print(f"Olá, {nome}! Seja bem vindo(a)!")

nome = input("digite seu nome: ")
saudar(nome)