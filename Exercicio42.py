# Exercício 42: Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
# Declarar
numerador: int = 1 
denominador: int = 1
# Inicio
while numerador <= 50:
    print("O valor da série atual é:", numerador / denominador,"; e o valor do numerador é:", numerador,"; e o valor do denominador é: ", denominador)
    numerador += 1
    denominador += 2
# Fim