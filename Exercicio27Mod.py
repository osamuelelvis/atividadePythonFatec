# Exercicio 27 (modularizado): Calcular velocidade da volta em uma pista circular
def calcular_velocidade(voltas, extensao, tempo, distancia, distancia_km, tempo_horas, velocidade):
    distancia = voltas * extensao
    distancia_km = distancia / 1000
    tempo_horas = tempo / 60
    velocidade = distancia_km / tempo_horas
    print("A velocidade média é igual a:", velocidade, "km/h")

def main(voltas, extensao, tempo):
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão da pista em metros: "))
    tempo = float(input("Digite o tempo gasto em minutos: "))
    calcular_velocidade(voltas, extensao, tempo, 0, 0, 0, 0)

if __name__ == "__main__":
    main(0, 0, 0)