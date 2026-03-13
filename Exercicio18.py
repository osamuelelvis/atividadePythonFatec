# Exercício 18: Programa que compara maior e menor
# Declarar
n1: int = int(input("Digite o primeiro número: "))  
n2: int = int(input("Digite o segundo número: "))
# Inicio
if n1 > n2:
    resultado = n1 - n2
    print("A diferença entre os números é:", resultado)
elif n2 > n1:
    resultado = n2 - n1
    print("A diferença entre os números é:", resultado)
# Fim