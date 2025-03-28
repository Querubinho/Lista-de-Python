#Peça três números ao usuário e informe qual é o maior e qual é o menor.

n1 = int(input("Diga um numero: "))
n2 = int(input("Diga outro numero: "))
n3 = int(input("Diga mais outro numero: "))

numeros = [n1, n2, n3]

def bubble_sort_desc(lista):
    n = len(lista)
    for i in range(n - 1):  
        for j in range(n - 1 - i):  
            if lista[j] < lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubble_sort_desc(numeros)

print(f"Lista do maior para o menor: {numeros}")
