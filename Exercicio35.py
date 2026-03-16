# Exercicio 35: Somatória dos números ímpares|
# Declarar
n1: int
n2: int
# Inicio
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = 0

if n1 > n2:
    for i in range(n2, n1 + 1, 1):
        if i % 2 != 0:
            resultado += i
else:
    for i in range(n1, n2 + 1, 1):
        if i % 2 != 0:
            resultado += i

print("A soma dos números ímpares entre", n1, "e", n2, "é:", resultado)
# Fim