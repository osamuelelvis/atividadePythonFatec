# Exercício 15: Cálculo da hipotenusa
import math
cateto1 = int(input("Digite o valor do primeiro cateto: "))
cateto2 = int(input("Digite o valor do segundo cateto: "))
hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))
print("O valor da hipotenusa é:", hipotenusa)