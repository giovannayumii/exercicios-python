print("3) 2. Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.")
print("Para encerrar a entrada de dados, deve ser digitado o valor zero;\tPara valores negativos, deve ser enviada uma mensagem;\tEsses valores (zero e negativos) não entrarão nos cálculos.")

numero=float(input('Digite um valor numérico - Zero para sair: '))
cont=0
while numero > 0:
  numero=float(input('Digite um valor numérico - Zero para sair: '))
  if numero <0:
    print("Esse número é negativo, digite outro")
    numero=float(input('Digite um valor numérico - Zero para sair: '))
  if cont == 0:
    maior=numero
    menor=numero
  elif numero >= maior:
    maior=numero
  elif numero <= menor:
    menor=numero
  cont=cont+1
print('Maior número= ',maior)
print('Menor número= ',menor) #precisa ajustar