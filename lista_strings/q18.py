nome = input("digite o seu nome: ")
email = input("digite o seu email: ")
password = input("digite uma senha: ")

def validar_nome(nome : str):
    if len(nome) < 3:
        return False
    
    for caractere in nome:
        if not (caractere.isalpha() or caractere.isspace()):
            return False
    
    return True

def validar_email(email : str):
    if " " in email:
        return False
    elif "@" not in email:
        return False
    elif "." not in email:
        return False
    
    return True

def validar_senha(password : str):
    if len(password) < 8:
        return False
    
    letra = False
    num = False

    
    for caractere in password:
        if caractere.isalpha():
            letra = True
        if caractere.isdigit():
            num = True
    
    return letra and num

if validar_nome(nome) and validar_email(email) and validar_senha(password):
    print("Cadastro aceito")
else:
    print("Cadastro recusado")