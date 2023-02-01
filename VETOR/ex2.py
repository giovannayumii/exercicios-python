print("2)Faça um programa que calcule e apresente a média de alturas de uma sala de 35 alunos. Informe também quantos alunos e quais (índice/posição) são os que possuem idade superior a 25 anos.​ Use dois vetores, um para altura e outro para idade. ")

vet_altura = []
vet_idade = []
soma_altura = 0
soma_idade=0
cont_maior25 = 0

for i in range(35):
  vet_idade.append (int(input ('Informe a Idade: ')))
  soma_idade = soma_idade + vet_idade[i]
  vet_altura.append (float(input('Informe a Altura: ')))
  soma_altura = soma_altura + vet_altura[i]
divisao=soma_altura / 35
print("Média da altura: %.2f "%divisao)

for i in range(35):

  if vet_idade[i] > 25:
    cont_maior25 += 1
    print('O aluno n°',i,'possui ',vet_idade[i],' anos')

print("Quantidade de alunos maiores de 25 anos: ",cont_maior25)