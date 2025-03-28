#Peça ao usuário três notas e calcule:
#a. A média aritmética simples
#b. A média ponderada considerando os pesos 2, 2 e 3
#c. A média ponderada considerando os pesos 1, 2 e 2

n1 = int(input("Diga o primeiro numero: "))
n2 = int(input("Diga o segundo numero: "))
n3 = int(input("Diga o terceiro numero: "))

media_arit = (n1 + n2 + n3) / 3

media_pond1 = (n1 * 2), (n2 * 2), (n3 * 3)

media_pond2 = (n1 * 1), (n2 * 2), (n2 * 2)

print("Media aritmetica:", media_arit)
print("Media ponderada peso 2, 2 e 3", media_pond1)
print("Media ponderada peso 1, 2 e 2:", media_pond2)
