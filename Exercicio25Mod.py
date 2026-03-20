# Exercicio 25 (modularizado): Hora de inicio e final de um jogo
# Declaração de variáveis
hora_inicio: int
minuto_inicio: int
hora_final: int
minuto_final: int

def calcular_duracao():
    inicio = (hora_inicio * 60) + minuto_inicio
    final = (hora_final * 60) + minuto_final
    if (final >= inicio):
        duracao = final - inicio
    else:
        duracao = (1440 - inicio) + final
    
    horas = duracao // 60
    minutos = duracao % 60
    print("O jogo durou", horas, "horas e", minutos, "minutos.")

def main():
    global hora_inicio, minuto_inicio, hora_final, minuto_final
    hora_inicio = int(input("Digite a hora de inicio do jogo: "))
    minuto_inicio = int(input("Digite o minuto de inicio do jogo: "))
    hora_final = int(input("Digite a hora final do jogo: "))
    minuto_final = int(input("Digite o minuto final do jogo: "))
    calcular_duracao()

if __name__ == "__main__":
    main()