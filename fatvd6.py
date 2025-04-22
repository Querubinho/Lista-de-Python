def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    count = 0
    for char in frase:
        if char in vogais:
            count += 1
    return count

frase = input("Digite uma palavra ou frase: ")
print(f"Quantidade de vogais: {contar_vogais(frase)}")
