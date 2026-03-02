# Exercicio 5: Equação de segundo grau
# Declarar
import math

a = int(input("Digite o valor de A: "));
b = int(input("Digite o valor de B: "));
c = int(input("Digite o valor de C: "));
# Início
delta = (b**2) - (4 * a * c);
print("O valor de delta é:", delta);

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print("X1:", x1)
print("X2:", x2)
# Fim