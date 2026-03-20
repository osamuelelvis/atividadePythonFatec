# Exercicio 22 (modularizado): Valores em ordem crescente
# Declaração de variáveis
n1: int
n2: int

def maior_menor2():
    if n1 > n2:
        print(f"O maior número é: {n1}")
        print(f"O menor número é: {n2}")
    else:
        print(f"O maior número é: {n2}")
        print(f"O menor número é: {n1}")

def main():
    global n1, n2
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    maior_menor2()

if __name__ == '__main__':
    main()