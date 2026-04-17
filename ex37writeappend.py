# Exercício 37: Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
# Declaração de variáveis
import os
os.makedirs('C:\\temp\\', exist_ok=True)
os.chmod('C:\\temp\\', 0o744)

dir = 'C:\\temp\\'
arq = 'ex37.txt'

def grava(termo, i):
    file_path = f"{dir}/{arq}"
    enc = 'utf-8'

    if (i == 0):
        tipo = 'w'
    else:
        tipo = 'a'

    with open(file_path, tipo, encoding=enc) as file:
        file.write(f"Termo {i + 1}: {termo}\n")
        
    print(f"Termo gravado: {termo}")

def main():
    n = int(input("Digite o número de termos da série de Fibonacci: "))

    a, b = 0, 1
    print(f"Fibonacci até o {n}º termo:")

    for i in range(n):
        print(a, end=" ")
        grava(a, i)
        a, b = b, a + b
    print()

if __name__ == '__main__':
    main()