# Exercício 41: Todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7
# Declarar
dado1: int
dado2: int
# Início
print("Possibilidades de 2 dados com soma igual a 7: ")
for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        if dado1 + dado2 == 7:
            print(f"Dado 1: {dado1}")
            print(f"Dado 2: {dado2}")
            print()
# Fim