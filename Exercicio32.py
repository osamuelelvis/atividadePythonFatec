# Exercicio 32: Mostrar fatorial de um número
# Declarar
c: int
f: int
n: int
# Inicio
n = int(input("Digite um número para calcular o fatorial: "))

f = 1
c = n

while c >= 1:
    f = f * c
    c = c - 1
    print("O valor de f é", f, "e o valor de c é", c)
    
print("O fatorial de", n, "é", f)
# Fim