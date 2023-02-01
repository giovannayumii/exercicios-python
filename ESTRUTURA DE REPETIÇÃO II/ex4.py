print("4)  Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.")

idade = int(input('Digite a idade - Zero para sair: '))
altura = float(input('Digite a altura: '))
media = 0
cont = 0

while idade > 0 and altura > 0:
  idade = int(input('Digite a idade - Zero para sair: '))
  altura = float(input('Digite a altura: ')) #precisa ajustar pra quando for 0 dar dar essa msg
  if idade > 20:
    media = media + altura
    cont = cont+1
media = media/cont
print('Média da altura com pessoas maiores de 20 anos= %.2f'%media)