# Exercício 45: Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
# Declarar
soma = 0.0
# Início
for i in range(1, 16):
    termo = i / (i ** 2)
    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo
    print("Termo: {:.4f}, Soma parcial: {:.4f}".format(termo, soma))

print(f"O resultado da série é: {soma:.4f}")
# Fim