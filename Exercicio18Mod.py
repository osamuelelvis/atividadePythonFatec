# Exercício 18 (modularizado): Programa que compara maior e menor
# Declaração de variáveis
def maior_menor():
    r: int
    if n1 > n2:
        r = n1 - n2
    else:
        r = n2 - n1
    print(f"A diferença entre os números é: {r}")

def main():
    global n1, n2
    n1 = int(input("Digite o primeiro número:  "))
    n2 = int(input("Digite o segundo número: "))
    maior_menor()

if __name__ == "__main__":
    main()