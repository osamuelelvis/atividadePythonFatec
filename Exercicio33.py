# Exercicio 33: Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
# Declarar
soma: int
n: int
c: int
# Inicio
soma = 0
n = int(input("Digite um número para calcular a série: "))
for i in range(1, n + 1, 1):
    soma = soma + (1 / i)
    print("O valor da soma é", soma, "e o valor de i é", i)

print("O resultado da série é:", soma)
# Fim