# Exercício 17: Cálculo do consumo de combustível
# Declarar
tempo_percurso = float(input("Digite o tempo gasto no percurso (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))
# Início
quantidade_gasta_litros = (velocidade_media * tempo_percurso) / 12  # Consumo de combustível: 1 litro a cada 12 km
print("A quantidade de combustível gasta no percurso é:", quantidade_gasta_litros, "litros")
# Fim