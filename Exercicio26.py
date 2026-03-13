# Exercicio 26: Múltiplo de um número
# Declarar
a: int
b: int
# Inicio
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if (a > b):
    maior = a
    menor = b
else:
    maior = b
    menor = a

if (maior % menor == 0):
    print("O número", maior, "é múltiplo de", menor)
else:
    print("O número", maior, "não é múltiplo de", menor)
# Fim