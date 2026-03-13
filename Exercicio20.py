# Exercicio 20: Equação do segundo grau
# Declarar
import math
a: float = float(input("Digite o valor de a: "))
b: float = float(input("Digite o valor de b: "))
c: float = float(input("Digite o valor de c: "))
# Início
delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.") 
elif delta == 0:
    raiz = -b / (2*a)
    print("A equação possui uma raíz real, que é: ", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("A equação possui duas raízes reais, que são: ", raiz1, "e", raiz2)
# Fim