# Exercicio 43: 43.	Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.
# Declarar
altura_ana = 1.10
altura_maria = 1.50
crescimento_ana = 0.03
crescimento_maria = 0.02
anos = 0
# Início
while altura_ana <= altura_maria:
    altura_ana += crescimento_ana
    altura_maria += crescimento_maria
    anos += 1
    print(f"Ano {anos}: Ana = {altura_ana:.2f} m, Maria = {altura_maria:.2f} m")

print(f"Após {anos} anos, Ana tem {altura_ana:.2f} m e Maria tem {altura_maria:.2f} m.")
# Fim