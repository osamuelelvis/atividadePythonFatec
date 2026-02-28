# Exercicio 13: Duração do alimento
quantidade_alimentos = float(input("Digite a quantidade de alimento (em quilos): "))
quantidade_alimentos_gramas = quantidade_alimentos * 1000
consumo_diario = 50
dias = quantidade_alimentos_gramas / consumo_diario
print("Esse alimento durará", dias, "dias")