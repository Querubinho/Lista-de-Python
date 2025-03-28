#Um cliente alugou um carro e rodou alguns quilômetros por um certo número de
#dias. O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de
#R$12 por km adicional. Calcule o valor total a ser pago.

distancia = int(input("Diga por quantos km's voce andou:"))
tempo = int(input("Diga por quantos dias voce alugou o carro:"))


if distancia > 100:
 taxa = (distancia - 100) * 12
 valor = tempo * 90 + taxa
 print(f"Quilometragem acima de 100, uma taxa foi aplicada. Valor: {valor}")

else:
 valor = tempo * 90
 print(f"Valor a ser pago: {valor}")
