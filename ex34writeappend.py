# Exercicio 34: Calcular tábuada
# Declaração de variáveis
import os
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

valor: int = 0
dir: str = ''
arq: str = ''

def main():
	global valor
	contador = 0
	result = 0
	
	valor = int(input("Digite um valor de 1 a 10: "))
	for i in range(1, 11, 1):
		contador = i
		result = mult(valor, contador)
		grava(contador, result)
	
def  mult(vlr, tab):
	res = (vlr * tab)
	return res
	
def grava(c, rslt):
	dir = '/tmp/exercicios'
	arq = 'ex34.txt'
	file: str = ''
	tipo: str = ''
	enc: str = ''
	linha: str = ''
	
	linha = str(rslt) + '\n'
	if (os.path.isdir(dir)):
		if (os.path.isfile(dir + '/' + arq)):
			if c > 0:
				tipo = 'a'
				
		else:
			tipo = 'w'
			
		enc = 'utf-8'
		file = open(dir + '/' + arq, tipo, encoding = enc)
		file.write(linha)
		file.close()
		
if __name__ == '__main__':
	main()