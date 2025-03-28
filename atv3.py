# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

valor = int(input("Diga o valor total das compras:"))

if valor > 500:
    taxa = (valor - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor acima de R$500. Valor com taxa de 50%: {valor_taxado}")

else:
    print("Livre de taxa")
