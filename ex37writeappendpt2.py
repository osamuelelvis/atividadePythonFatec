# Exercício 37: Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
# Declaração de variáveis
import os
os.makedirs('C:\\temp\\', exist_ok=True)
os.chmod('C:\\temp\\', 0o744)

dir = 'C:\\temp\\'
arq = 'ex37.txt'

def valida_impar(numero):
    if numero % 2 != 0:
        return numero
    return -1

def leitura():
    file_path = f"{dir}{arq}"
    enc = 'utf-8'

    with open(file_path, 'r', encoding=enc) as file:
        for linha in file:
            partes = linha.strip().split(':')
            if len(partes) == 2:
                numero = int(partes[1].strip())
                resultado = valida_impar(numero)
                if resultado != -1:
                    print(resultado)

def main():
    leitura()

if __name__ == '__main__':
    main()