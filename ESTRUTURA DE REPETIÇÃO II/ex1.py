print("1) Construir um algoritmo para calcular a soma de um conjunto de valores inteiros positivos. Digitar zero para sair.")

numero=int(input('Digite um valor numérico - Zero para sair: '))
soma_numeros=0
while numero > 0:
  soma_numeros=soma_numeros+numero
  numero=int(input('Digite um valor numérico-zero para sair: '))
print('Soma = ',soma_numeros)