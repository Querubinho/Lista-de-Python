# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

login = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while login == senha:
    print("Sua senha e login nao podem ser iguais, tente de novo.")
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

else:
    print("Conta criada!")
