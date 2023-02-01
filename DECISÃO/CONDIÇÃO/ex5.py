print("5) Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de classificar em uma das seguintes categorias:")
print("infantil = 5 - 10 anos;\tjuvenil = 11-17 anos;\tadulto = maiores de 18 anos.")

print("Informe a idade do nadador")
idade=int(input())
if idade >= 5 and idade <=10:
  print("Categoria infantil")
elif idade >=11 and idade <= 17:
  print("Categoria juvenil")
else:
  print("Categoria adulto")