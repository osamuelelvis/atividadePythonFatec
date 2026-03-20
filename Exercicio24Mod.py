# Exercício 24 (modularizado): Exercicio 24: Valor divisivel por 2 ou 3
# Declaração de variáveis
numero: int

def verificar_divisibilidade():
    if numero % 2 == 0 and numero % 3 == 0:
        print("O número é divisível por 2 e por 3.")
    elif numero % 2 == 0:
        print("O número é divisível por 2.")
    elif numero % 3 == 0:
        print("O número é divisível por 3.")
    else:
        print("O número não é divisível por 2 nem por 3.")

def main():
    global numero
    numero = int(input("Digite um número inteiro: "))
    verificar_divisibilidade()
if __name__ == "__main__":
    main()