print("17) Faça um programa que receba duas notas de seis alunos. Calcule e mostre:\ta média aritmética das duas notas de cada aluno;\t e a mensagem que está na tabela a seguir:")
print("Média aritimética      Mesagem")
print()
print("Até 3                  Reprovado")
print("Entre 3 e 7	           Exame")
print("De 7 para cima	       Aprovado")

print("o total de alunos aprovados;\to total de alunos de exame;\to total de alunos reprovados;\ta média da classe.")

alunos=0
total_aprovados=0
total_exame = 0
total_reprovados = 0
soma_media_classe = 0
while alunos < 6:
  p1 = float(input('Informe a nota da primeira prova: '))
  p2 = float(input('Informe a nota da segunda prova: '))
  media = (p1 + p2) / 2
  if media <= 3:
    print('Reprovado, você tirou média = ',media)
    total_reprovado=total_reprovado+1
  elif media > 3 and media < 7:
    print('Exame, você tirou média = ',media)
    total_exame = total_exame+1
  else:
    print('Aprovado, você tirou média = ',media)
    total_aprovados=total_reprovados+1
  soma_media_classe= soma_media_classe+media
  alunos = alunos+1
media_classe = soma_media_classe / alunos   
print('Quantidade de alunos',alunos)
print('Total de alunos aprovados',total_aprovados)
print('Total de alunos reprovados',total_reprovado)
print('Total de alunos aprovados',total_exame)
print(f'Média da classe {media_classe:.2f}')