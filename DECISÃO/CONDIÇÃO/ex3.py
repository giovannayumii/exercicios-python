print("3) Tendo como dados de entrada a altura e o sexo (M/F) de uma pessoa (M-masculino ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:")
print("homem: (72.7 * altura) - 58;\tmulher: (62.1 * altura) - 44.7")
print("Digite o sexo da pessoa(M para masculino e F para feminino):")
sexo=input( )
print("Digite a altura da pessoa:")
altura=float(input())
if sexo=='M' or sexo=='m':
  homem= (72.7 * altura) - 58
  print("O peso ideal é %.2f"%homem)
else:
  mulher= (62.1 * altura) - 44.7
  print("O peso ideal é %.2f"%mulher)