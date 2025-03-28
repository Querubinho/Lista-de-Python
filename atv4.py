# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

distancia = int(input("Diga quantos quilometros voce andou:"))
tempo = int(input("Diga por quantos dias voce alugou o carro:"))


if distancia > 100:
 taxa = (distancia - 100) * 12
 valor = tempo * 90 + taxa
 print(f"Quilometragem acima de 100, taxa adicionada ao valor. Total: {valor}")

else:
 valor = tempo * 90
 print(f"Valor a ser pago: {valor}")
