# Exercício 20 (modularizado): Equação do segundo grau 
import math
# Declaração de variáveis
a: int
b: int
c: int
raiz1: float
raiz2: float

def equacao_segundograu():
    global raiz1, raiz2
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz1 = -b / (2*a)
        print(f"A equação possui uma raíz real: {raiz1}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

def main():
    global a, b, c
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    equacao_segundograu()

if __name__ == "__main__":
    main()