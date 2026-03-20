# Exercício 39:	Calcule a quantidade de grãos contidos em um tabuleiro de xadrez
# Declarar
casa: int
quantidade: int = 1
total: int = 0
# Início
for casa in range(1, 65):
	total += quantidade
	if casa < 64:
		quantidade *= 2

print(f"Quantidade na casa 64: {quantidade}")
print(f"Total de grãos no tabuleiro: {total}")
# Fim