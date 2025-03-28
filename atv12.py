#Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a
#média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos.

turmas = int(input("Informe a quantidade de turmas: "))
alunos = int(input("Informe a quantidade total de alunos: "))

media = alunos // turmas

if media > 40:
    print(f"Atencao, a media é superior a 40 alunos, sendo {media} alunos.")

else:
 print(f"A media de alunos por turma é {media}.")
