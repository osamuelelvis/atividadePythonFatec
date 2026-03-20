# Exercicio 29 (modularizado): Investimento em poupança ou renda fixa
def calcular_investimento(opcao, valor_investido, valor_final):
    if (opcao == 1):
        print("Opção escolhida: poupança")
        valor_final = valor_investido * 1.03 * 1
    elif (opcao == 2):
        print("Opção escolhida: renda fixa")
        valor_final = valor_investido * 1.05 * 1
    else:
        print("Opção inválida! Digite 1 para poupança ou digite 2 para renda fixa.")

    print("Após 30 dias, o valor final do investimento será de:", valor_final)

def main(opcao, valor_investido, valor_final):
    print("Seja bem vindo! Digite 1 para poupança ou digite 2 para renda fixa.")
    opcao = int(input("Digite sua opção: "))
    print("Quanto vai ser investido? ")
    valor_investido = float(input("Digite o valor a ser investido: "))
    calcular_investimento(opcao, valor_investido, valor_final)

if __name__ == "__main__":
    main(0, 0, 0)