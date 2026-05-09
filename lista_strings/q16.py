#Crie uma função chamada limpar_frase que receba uma frase e retorne uma nova frase contendo apenas letras e espaços. Caracteres como números, pontos, vírgulas, exclamações e símbolos devem ser removidos.
def limpar_frase(frase : str):
    nova_frase = ""
    for caractere in frase:
        if caractere.isalpha() or caractere.isspace():
            nova_frase += caractere
    
    return nova_frase

frase = input("digite uma frase: ")

print(limpar_frase(frase))