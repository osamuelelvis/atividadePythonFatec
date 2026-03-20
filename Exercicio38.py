# Exercício 38: Receba 100 números reais e mostre o maior e o menor valor (somente positivos).
# Declarar
contador = 0
maior = float
menor = float
# Início
while contador < 100:
    num = float(input(f"Digite o {contador + 1}º número positivo: "))

    if num <= 0:
        print("Valor inválido. Digite apenas número positivo.")
        continue

    if maior is float or num > maior:
        maior = num

    if menor is float or num < menor:
        menor = num

    contador += 1

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
# Fim