print("9) Elabore um algoritmo que calcule e informe a média de idades de 5 alunos.")

idades = 0
cont = 0

while cont < 5:
  print("Digite a idade:")
  idade = int(input())
  idades = idades + idade
  cont = cont + 1
idades_media=idades/5
print("A média de idades é %d"%idades_media)