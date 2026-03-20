
# Exercício 19 (modularizado): 
n1: int
n2: int

def ma_me():
    if n1 > n2:
        print(f"O maior número é: {n1}")
    else:
        print(f"O maior número é: {n2}")

def main():
    global n1, n2
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    ma_me()

if __name__ == "__main__":
    main()