# Exercicio 25: Hora de inicio e final de um jogo
# Declarar
hora_inicio = int(input("Digite a hora de inicio do jogo: "))
minuto_inicio = int(input("Digite o minuto de inicio do jogo: "))
hora_final = int(input("Digite a hora final do jogo: "))
minuto_final = int(input("Digite o minuto final do jogo: "))
# Inicio
inicio = (hora_inicio * 60) + minuto_inicio
final = (hora_final * 60) + minuto_final
if (final >= inicio):
    duracao = final - inicio
else:
    duracao = (1440 - inicio) + final

horas = duracao // 60
minutos = duracao % 60
print("O jogo durou", horas, "horas e", minutos, "minutos.")
# Fim