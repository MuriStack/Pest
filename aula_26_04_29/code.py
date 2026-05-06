def verificar_str(string : str):
    for carac in range(len(string)):
        if string[carac] == "a" or string[carac] == "A":
            return True 
    return False

def contar_as(string : str):
    contador = 0
    for carac in range(len(string)):
        if string[carac] == "a" or string[carac] == "A":
            contador += 1
    return contador

string = input("digite uma string: ")

if verificar_str(string) == True:
    print("Tem A na minha string")
else:
    print("Não tem A na minha string")

if contar_as(string) > 0:
    print(f"Tem {contar_as(string)} AS na minha string ")
else:
    print("Tem 0 AS na minha string")