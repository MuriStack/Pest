def cria_fruta(x : str, y : str):
    xy = x[0] + y[-1] 
    return xy

fruit1 = input("digite uma fruta: ")
fruit2 = input("digite outra fruta: ")

salada_fruta = cria_fruta(fruit1,fruit2)
print(salada_fruta)