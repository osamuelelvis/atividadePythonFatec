# Exercicio 36: Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!.
# Declaração de variáveis
import os
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

soma: float
n: int
fatorial: int

def fatorial(n):
    fatorial = 1

    for i in range(1, n + 1, 1):
        fatorial *= i
    return fatorial

def divisao(a, b):
    return a / b

def grava(termo, resultado_final):
    dir = '/tmp/exercicios'
    arq = 'ex36.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    if resultado_final is None:
        linha = str(termo) + '\n'
    else:
        linha = 'Resultado final: ' + str(resultado_final) + '\n'

    if os.path.isdir(dir):
        if os.path.isfile(dir + '/' + arq):
            tipo = 'a'
        else:
            tipo = 'w'

        enc = 'utf-8'
        file = open(dir + '/' + arq, tipo, encoding=enc)
        file.write(linha)
        file.close()

def main():
    n = int(input("Digite um número para calcular a série: "))
    if n < 0:
        print("Número inválido! Digite um número inteiro não negativo.")
    else:
        soma = 1.0

        for i in range(1, n + 1, 1):
            fat = fatorial(i)
            termo = divisao(1, fat)
            soma += termo
            grava(termo, None)

        grava(None, soma)

if __name__ == "__main__":
    main()