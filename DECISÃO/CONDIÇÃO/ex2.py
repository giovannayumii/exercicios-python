print("2) Faça um algoritmo que leia o nome e a idade de uma pessoas, verifique se a idade de uma pessoa é menor ou maior de idade. Considera-se maior de idade uma pessoa com 18 anos ou mais. Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela é ou não maior de idade.")

print("Digite o nome:")
nome=input()
print("Digite a idade:")
idade=int(input())
if idade >=18:
  print("maior de idade")
else: 
  print("Menor de idade")