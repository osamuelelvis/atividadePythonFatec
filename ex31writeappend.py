# Exercicio 31: Quadrados entre 10 e 150
# Declaração de variáveis
import os
os.makedirs('C:\\temp\\', exist_ok=True)
os.chmod('C:\\temp\\', 0o744)

def grava(pares):
    dir = 'C:\\temp\\'
    arq = 'ex31.txt'
    file_path = f"{dir}/{arq}"
    tipo = 'w'
    enc = 'utf-8'

    with open(file_path, tipo, encoding=enc) as file:
        file.write("Números gravados:\n")
        for numero, quadrado in pares:
            file.write(f"Quadrado de {numero}: {quadrado}\n")

    print(f"Os números foram gravados no arquivo '{file_path}'.")

def main():
    pares = []
    for n in range(10, 151, 1):
        a = n * n
        pares.append((n, a))

    grava(pares)

if __name__ == '__main__':
    main()
