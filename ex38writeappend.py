# Exercício 38: Receba 100 números reais e mostre o maior e o menor valor (somente positivos).
# Declaração de variáveis
import os
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

numeros = []
maior = None
menor = None
dir = '/tmp/exercicios'
arq = 'ex38.txt'

def main():
    global numeros, maior, menor, dir, arq
    contador = 0

    while contador < 5:
        try:
            num = float(input(f"Digite o {contador + 1}º número positivo: "))
            if num <= 0:
                print("Valor inválido. Digite apenas número positivo.")
                continue
            numeros.append(num)
            contador += 1
        except ValueError:
            print("Valor inválido! Digite um número real.")

    maior = max(numeros)
    menor = min(numeros)
    grava()

def grava():
    global numeros, maior, menor, dir, arq
    file_path = f"{dir}/{arq}"
    tipo = 'w'
    enc = 'utf-8'

    with open(file_path, tipo, encoding=enc) as file:
        file.write("Números fornecidos:\n")
        for num in numeros:
             file.write(f"{num}\n")
        file.write(f"\nMaior valor: {maior}\n")
        file.write(f"Menor valor: {menor}\n")

    print(f"Os números e os resultados foram gravados no arquivo '{file_path}'.")

if __name__ == '__main__':
	main()