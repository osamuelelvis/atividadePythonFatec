# Exercicio 34: Calcular tábuada
# Declarar
numero_usuario: int
i: int
resultado: int
# Inicio
numero_usuario = int(input("Digite um número para calcular a tabuada: "))

for i in range(1, 11, 1):
    resultado = numero_usuario * i
    print(numero_usuario, "x", i, "=", resultado)
# Fim