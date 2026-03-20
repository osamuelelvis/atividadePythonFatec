# Exercício 40: Números primos existentes entre valores informados pelo usuário.
# Declarar
n1: int
n2: int
# Início
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
print(f"Números primos entre {n1} e {n2}:")
for num in range(n1, n2 + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()
# Fim