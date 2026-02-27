# Exercicio 6: Troca de valores x e y
x = input("Digite o valor de X: ");
y = input("Digite o valor de Y: ");

x, y = y, x;

print("Após a troca:");
print("Valor de X:", x);
print("Valor de Y:", y);