print("----- find() e index()")

str = "Cena Oculta"

indice1 = str.find("c")
indice2 = str.index("c") 

print(indice1)
print(indice2)

indice1 = str.find("x") #Mostra -1
indice2 = str.index("x") #Dá erro

print(indice1)
print(indice2)