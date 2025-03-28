# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

salario_inicial = int(input("Informe seu salario inicial: "))
tempo = int(input("Informe o tempo que voce trabalha: "))

salario_final = salario_inicial * (2 ** tempo)

print(f"Seu salario apos {tempo} anos de servico sera: {salario_final}.")
