# Exercicio 21: Média de quatro números
# Declaração de variáveis
import os
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

nome: str = ''
nota1: float
nota2: float
nota3: float
nota4: float
valor_media: float
dir: str = ''
arq: str = ''

def main():
    contador = 0

    for i in range(1, 6, 1):
        contador = i
        print(f"Aluno {contador}")
        entrada()

def entrada():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input("Informe o nome do aluno:")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    media = med(nota1, nota2, nota3, nota4)
    valor_media = media
    print("A média é:", media)
    
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def med(nota1, nota2, nota3, nota4):
    media: float
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

def cadastro(nome, nota1, nota2, nota3, nota4, valor_media):
    global dir
    global arq
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'
    linha: str = ''

    linha = f"{nome}; {nota1}; {nota2}; {nota3}; {nota4}; {valor_media}\n"
    escreveArq(dir, arq, linha)

def escreveArq(dir, arq, linha):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    if (os.path.isdir(dir)):
        if (os.path.isfile(dir + '/' + arq)):
            tipo = 'a'
        else:
            tipo = 'w'

        enc = 'utf-8'
        file = open(dir + '/' + arq, tipo, encoding=enc)
        file.write(linha)
        file.close()

if __name__ == '__main__':
    main()