# Exercício 21 (modularizado): Média de quatro números
# Declaração de variáveis
nota1: float
nota2: float
nota3: float
nota4: float
media_final: float

def calcular_media():
    global media_final
    media_final = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média é: {media_final}")

def main():
    global nota1, nota2, nota3, nota4
    nota1 = int(input("Informe a primeira nota: "))
    nota2 = int(input("Informe a segunda nota: "))
    nota3 = int(input("Informe a terceira nota: "))
    nota4 = int(input("Informe a quarta nota: "))
    calcular_media()

if __name__ == "__main__":
    main()