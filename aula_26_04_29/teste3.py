def tamanho_string(string1 : str, string2 : str):
    len1 = len(string1)
    len2 = len(string2)
    if len1 > len2:
        print(f"{string1} é maior que a palavra {string2}")
    elif len2 > len1:
        print(f"{string2} é maior que a palavra {string1}")
    else:
        print(f"{string1} é igual a palavra {string2}")

word1 = input("digite a string1: ")
word2 = input("digite a string2: ")

tamanho_string(word1,word2)