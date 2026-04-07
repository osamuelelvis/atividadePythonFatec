# Exercício 38: Receba 100 números reais e mostre o maior e o menor valor (somente positivos).
# Declaração de variáveis
import os
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

numeros = []
maior = None
menor = None
dir = '/tmp/exercicios'
arq = 'ex38pt2.txt'

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
    processa_multiplos()

def grava():
    global numeros, maior, menor, dir, arq
    file_path = f"{dir}/{arq}"
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for num in numeros:
            file.write(f"{num}\n")
        file.write(f"\nMaior: {maior}\n")
        file.write(f"Menor: {menor}\n")
    
    print(f"Números gravados em '{file_path}'.")

def processa_multiplos():
    global dir, arq
    file_path = f"{dir}/{arq}"
    output_path = f"{dir}/multiplos_de_5.txt"

    with open(file_path, 'r', encoding='utf-8') as file:
        with open(output_path, 'w', encoding='utf-8') as output:
            for linha in file:
                linha = linha.strip()
                try: 
                    numero = float(linha)
                    if numero % 5 == 0:
                        output.write(f"{int(numero)}\n")
                except ValueError:
                    continue

    print(f"Múltiplos de 5 gravados em '{output_path}'.")

if __name__ == '__main__':
	main()