# Erick Raphael - 3º ano B  
# Atividade para a professora Letícia  

turmas = int(input("Informe a quantidade de turmas: "))
alunos = int(input("Informe a quantidade total de alunos: "))

media = alunos // turmas

if media > 40:
    print(f"Atencao, a media é superior a 40 alunos, sendo {media} alunos.")

else:
 print(f"A media de alunos por turma é {media}.")
