# Exercicio 26 (modularizado): Múltiplo de um número
# Declaração de variáveis
a: int
b: int

def calcular_multiplo():
    if (a > b):
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    resultado = maior % menor
    print("O resto da divisão é", resultado)

    if (maior % menor == 0):
        print("O número", maior, "é múltiplo de", menor)
    else:
        print("O número", maior, "não é múltiplo de", menor)

def main():
    global a, b
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    calcular_multiplo()

if __name__ == "__main__":
    main()