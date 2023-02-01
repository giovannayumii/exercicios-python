print("4) Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.")

print("Digite um número")
n=int(input())
if n%2==0:
  print("par")
else:
  print("impar")
if n<0:
  print("negativo")
else:
  print("positivo")