def soma(n1, n2):
    soma = n1 + n2
    return soma

def sub(n1, n2):
    sub = n1 - n2
    return sub

def mult(n1, n2):
    mult = n1 * n2
    return mult

def div(n1, n2):
    div = n1 / n2
    return div

n1 = int(input("Fala um número ai: "))
n2 = int(input("Fala outro número ai: "))
op = input("Escolhe uma operação ai: ")

s = soma(n1, n2)
sb = sub(n1, n2)
m = mult(n1, n2)
d = div(n1, n2)

if op == 's':
    print(f"A resposta da soma é: {s}")
    
elif op == 'sb':
    print(f"A resposta da subtração é: {sb}")
    
elif op == 'm':
    print(f"A resposta da multiplicalção é: {m}")
    
elif op == 'd4':
    print(f"A resposta da divisão é: {d}")
    
else:
    print("Operação inválida!")
