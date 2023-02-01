print("2) Construir um algoritmo para calcular a média aritmética de um conjunto de valores inteiros positivos. Digitar zero para sair.")

numero = int(input('Digite um valor numérico - Zero para sair: '))
soma_numeros = 0
cont = 0
while numero > 0:
  soma_numeros = soma_numeros+numero
  numero = int(input('Digite um valor numérico-zero para sair: '))
  cont = cont +1
  divisao = soma_numeros / cont
print('Soma = ',soma_numeros)
print(divisao)