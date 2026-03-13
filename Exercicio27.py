# Exercicio 27: Calcular velocidade da volta em uma pista circular
# Declarar
voltas: int
extensao: float
tempo: float
# Inicio
voltas = int(input("Digite o número de voltas: "))
extensao = float(input("Digite a extensão da pista em metros: "))
tempo = float(input("Digite o tempo gasto em minutos: "))

distancia = voltas * extensao
distancia_km = distancia / 1000
tempo_horas = tempo / 60
velocidade = distancia_km / tempo_horas

print("A velocidade média é igual a:", velocidade, "km/h")
# Fim