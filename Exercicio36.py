# Exercicio 36: Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!.
# Declarar
soma: float
n: int
fatorial: int
# Inicio
n = int(input("Digite um número para calcular a série: "))

if n < 0:
    print("Número inválido! Digite um número inteiro não negativo.")

else:
    soma = 1.0
    fatorial = 1

    for i in range(1, n + 1, 1):
        fatorial *= i
        soma += 1 / fatorial
        print("O valor da soma é", soma, "e o valor de i é", i)

    print("O resultado da série é:", soma)
# Fim