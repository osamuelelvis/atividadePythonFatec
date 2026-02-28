# Exercício 16: Cálculo do salário
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))
percentual_de_desconto = float(input("Digite o percentual de desconto (em %): "))
numero_de_descendentes = int(input("Digite o número de descendentes: "))
salario_bruto = horas_trabalhadas * valor_por_hora
salario_liquido = salario_bruto - (salario_bruto * (percentual_de_desconto / 100)) + (numero_de_descendentes * 100)
print("O salário a receber é:", salario_liquido)