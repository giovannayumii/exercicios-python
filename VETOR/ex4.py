print("4) Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala.")

media_alunos=[]
soma=0
for i in range(10):
    media_alunos.append(float(input("Digite a média do aluno: ")))
    soma = soma + media_alunos[i]
media=soma/len(media_alunos)
print("Média da sala: ",media)

acima_da_media=0
abaixo_da_media=0
for i in range(10):
    if media_alunos[i] >= media:
        acima_da_media = acima_da_media + 1
    else:
        abaixo_da_media = abaixo_da_media + 1
print("Quantidade de alunos acima da média da sala: ", acima_da_media)
print("Quantidade de alunos abaixo da média da sala: ",abaixo_da_media)