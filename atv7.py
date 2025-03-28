# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

num = int(input("Diga um numero impar:"))

anterior = num - 2
num_anterior = anterior * anterior

posterior = num + 2
num_posterior = posterior * posterior

dif_anterior = num_anterior - num 
dif_posterior = num_posterior - num

print(f"Diferenca do quadrado do anterior: {dif_anterior}.")
print(f"Diferenca do quadrado do posterior: {dif_posterior}.")
