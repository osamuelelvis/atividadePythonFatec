# Exercicio 28 (modularizado): Calcular e mostrar o novo preço

def calcular_novo_preco(preco_atual, media_mensal, preco_novo):
    if (media_mensal < 500 and preco_atual < 30):
        preco_novo = preco_atual * 1.10
    elif (media_mensal >= 500 and preco_atual >= 30 and preco_atual < 80):
        preco_novo = preco_atual * 1.15
    elif (media_mensal >= 1000 and preco_atual >= 80):
        preco_novo = preco_atual * 0.95
    else:
        preco_novo = preco_atual
        
    print("O novo preço do produto é:", preco_novo)

def main(preco_atual, media_mensal):
    preco_atual = float(input("Digite o preço atual do produto: "))
    media_mensal = float(input("Digite a média mensal de vendas do produto: "))
    calcular_novo_preco(preco_atual, media_mensal, 0)

if __name__ == "__main__":
    main(0, 0)