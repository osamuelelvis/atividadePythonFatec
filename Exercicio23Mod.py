# Exercício 23 (modularizado): Valores em ordem crescente - pt.2
# Declaração de variáveis
valor1: int
valor2: int
valor3: int
valor4: int
numero: list

def ordem_crescente():
    global numero
    numero = [valor1, valor2, valor3, valor4]
    numero.sort()
    print(f"Os números em ordem crescente são: {numero}")

def main():
    global valor1, valor2, valor3, valor4
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))
    valor4 = int(input("Digite o quarto valor: "))
    ordem_crescente()

if __name__ == "__main__":
    main()