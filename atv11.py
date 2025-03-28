#Crie um sistema de login que não permite que o nome de usuário e a senha sejam iguais.

user = input("Informe seu login: ")
senha = input("Informe sua senha: ")

while user == senha:
    print("Sua senha e login nao podem ser iguais, tente de novo.")
    user = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

else:
    print("Conta criada!")
