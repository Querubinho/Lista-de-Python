#Crie um programa que gere e exiba os 100 primeiros números primos.

def analise_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
num = 2

while len(primos) < 100:
    if analise_primo(num):
        primos.append(num)
    num += 1

print(" ".join(map(str, primos)))
