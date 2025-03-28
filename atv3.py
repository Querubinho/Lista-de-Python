#Peça ao usuário o valor total das mercadorias compradas. Se for menor que R$500,
#não há imposto. Caso contrário, aplique uma taxa de 50% sobre o valor que ultrapassar
#os R$500.

valor = int(input("Diga o valor das compras:"))

if valor > 500:
    taxa = (valor - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor acima de R$500. Valor com taxa de 50%: {valor_taxado}")

else:
    print("Livre de taxa")
