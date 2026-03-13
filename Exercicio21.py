# Exercicio 21: Média de quatro números
# Declarar
numero: int
soma: int = 0
# Início
for i in range(4):
    numero = int(input("Informe a nota: "))
    soma += numero
    media = soma / 4

print("A média é:", media)
if (media >= 6):
    print("APROVADO!")
elif (media >= 3):
    print("EXAME!")
else:
    print("RETIDO!")
# Fim