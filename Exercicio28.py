# Exercicio 28: Calcular e mostrar o novo preço
# Declarar
preco_atual: float
media_mensal: float
# Inicio
preco_atual = float(input("Digite o preço atual do produto: "))
media_mensal = float(input("Digite a média mensal de vendas do produto: "))

if (media_mensal < 500 and preco_atual < 30):
    preco_novo = preco_atual * 1.10
elif (media_mensal >= 500 and preco_atual >= 30 and preco_atual < 80):
    preco_novo = preco_atual * 1.15
elif (media_mensal >= 1000 and preco_atual >= 80):
    preco_novo = preco_atual * 0.95
else:
    preco_novo = preco_atual

print("O novo preço do produto é:", preco_novo)
# Fim