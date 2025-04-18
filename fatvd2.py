def km(n1):
    
    return n1 * 0.621371

def m(n1):
    
    return n1 * 100

def l(n1):
    
    return n1 * 1000

n1 = input("digite um valor em km, m ou l: ")
op = input("digite a unidade de medida (km, m ou l): ")

if op == "km":
    print(f"{n1} km é igual a {km(n1)} milhas")
    
elif op == "m":
    print(f"{n1} m é igual a {m(n1)} cm")
    
elif op == "l": 
    print(f"{n1} l é igual a {l(n1)} ml")
    
else:
    print("unidade de medida inválida")
