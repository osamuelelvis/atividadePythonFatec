# Exercício 37: Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
# Declarar
n: int
# Início
n = int(input("Digite o número de termos da série de Fibonacci: "))

a, b = 0, 1
print(f"Fibonacci até o {n}º termo:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
# Fim