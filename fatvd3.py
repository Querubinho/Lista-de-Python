def contar_caracteres(frase):
    return len(frase.replace(" ", ""))

frase = input("Digite uma frase: ")
print(f"A frase possui {contar_caracteres(frase)} caracteres (sem espaços).")
