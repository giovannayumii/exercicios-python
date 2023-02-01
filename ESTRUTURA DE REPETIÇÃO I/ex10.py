print("10) Construir um algoritmo para calcular a média aritmética de preços de 5 produtos.")

preco_produtos=0
cont=0
while cont <5:
  print("Digite o preço do produto:")
  preco_produto=float(input())
  preco_produtos= preco_produtos+preco_produto
  cont=cont+1
media=preco_produtos/5
print("A média de preço dos 5 produtos é R$ %.2f"%media)