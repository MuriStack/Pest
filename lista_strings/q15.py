#Uma loja usa códigos de produto com as seguintes regras: Deve ter exatamente 6 caracteres, os 2 primeiros caracteres devem ser letras, os 4 últimos caracteres devem ser números, crie uma função chamada validar_codigo que receba um código e retorne se ele é válido ou inválido.
def validar_codigo(codigo : str):
    if len(codigo) == 6 and codigo[:2].isalpha() and codigo[2:].isdigit():
        return "válido"
        
    return "inválido"

codigo = input("digite um código: ")

print(validar_codigo(codigo))