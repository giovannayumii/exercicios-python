print("1) Faça um programa que calcule e apresente a média de idades de uma sala de 35 alunos.​​")

i = 0
vet_idade = []
print("Inserindo/cadastrando valores no vetor de idade............com while.......")
while i < 5:
    vet_idade.append(int(input('Informe a idade: ')))
    i = i + 1
i = 0
print("Apresentando valores cadastrados/inseridos do vetor de idade..........com while ........")
while i < len(vet_idade):
    print(vet_idade[i],end='  ')
    i = i + 1

#-----------------------------------------------------------------------------

vet_idade = []
print("\nInserindo/cadastrando valores no vetor de idade........... com for .......")
for p in range(5):
    vet_idade.append(int(input('Informe a idade: ')))

print("\nApresentando valores cadastrados/inseridos do vetor de idade..........com for ........")
for p in range( len(vet_idade)  ):
    print(vet_idade[p],end='  ')