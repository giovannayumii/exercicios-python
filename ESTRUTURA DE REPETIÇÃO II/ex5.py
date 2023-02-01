print("No final do ano muitas pessoas compram presentes. Faça um programa que registre as pessoas, usando como critério de parada a letra ‘n’, para a pergunta “Deseja cadastrar outro (‘s’/’n’)?”, para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:")
print("Quantidade de mulheres e de homens;\tQuantidade de mulheres e de homens abaixo e acima de 18 anos;\tQuantidade de mulheres e de homens acima de 60 anos.")

mulheres=0
homens=0
mulheres_acima_18anos=0
mulheres_abaixo_18anos=0
homens_acima_18anos=0
homens_abaixo_18anos=0
mulheres_mais_60=0
homens_mais_60=0
mulher=0
homem=0
print("Deseja fazer um cadastro?")
cadastro=input()
while cadastro=='S' or cadastro =='s':
  print("Digite o sexo: F ou M")
  sexo=input()  
  print("Qual a idade?")
  idade=int(input())
  print("deseja cadastrar outro?")
  cadastro=input()
  if sexo =='M'or sexo=='m':
    if idade <=18:
      homens_abaixo_18anos+=1
    elif idade >18 and idade<=60:
      homens_acima_18anos+=1
    elif idade>60:
      homens_mais_60+=1
    homens=homens+1
  elif sexo=='F' or sexo=='f':
    if idade <18 or idade ==18:
      mulheres_abaixo_18anos+=1
    elif idade >18 and idade <=60:
      mulheres_acima_18anos+=1
    elif idade>60:
      mulheres_mais_60+=1
    mulheres=mulheres+1
print("Quantidade de mulheres: ",mulheres)
print("Quantidade de homens: ",homens)
print("Quantidade de mulheres com 18 anos ou menos: ",mulheres_abaixo_18anos)
print("Quantidade de homens com 18 anos ou menos: ",homens_abaixo_18anos)
print("Quantidade de mulheres com mais de 18 anos: ",mulheres_acima_18anos)
print("Quantidade de homens com mais de 18 anos: ",homens_acima_18anos)
print("Quantidade de mulheres com mais de 60 anos: ",mulheres_mais_60)
print("Quantidade de homens com mais de 60 anos: ",homens_mais_60)