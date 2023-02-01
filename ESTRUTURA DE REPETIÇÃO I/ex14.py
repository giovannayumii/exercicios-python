print("14) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:")
print("nome da cidade;\tnúmero de veículos de passeio;\tnúmero de acidentes de trânsito com vítimas.")
print("Deseja-se saber: \to maior índice de acidentes de trânsito e a que cidades pertence;\t o menor índice de acidentes de trânsito e a que cidades pertence;\tqual é a média de veículos nas cinco cidades juntas;\tqual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.")

somatoria_veiculos_cidades = 0
total_cidades = 0
numero_cidades_2000_veiculos = 0

for cidade in range(3):

  nome_cidade=input("Digite o nome da cidade: ")
  numero_veiculos=int(input("Digite o número de veiculos: "))

  if numero_veiculos < 2000:
    numero_cidades_2000_veiculos = numero_cidades_2000_veiculos +1
    
  numero_acidentes=int(input("Digite o número de acidentes: "))
  total_cidades = total_cidades + 1
  
  if cidade == 0:
    maior_casos_acidentes = numero_acidentes
    cidade_maior_casos_acidentes = nome_cidade
    menor_casos_acidentes = numero_acidentes
    cidade_menor_casos_acidentes = nome_cidade
    
  elif numero_acidentes > maior_casos_acidentes:
    maior_casos_acidentes = numero_acidentes
    cidade_maior_casos_acidentes = nome_cidade
    
  elif numero_acidentes < menor_casos_acidentes:
    menor_caso_acidentes = numero_acidentes
    cidade_menor_casos_acidentes = nome_cidade
    
  somatoria_veiculos_cidades = somatoria_veiculos_cidades + numero_veiculos

  media_carros_cidades = somatoria_veiculos_cidades / total_cidades

  if numero_veiculos < 2000:
    soma_acidentes_cidades_2000_veiculos = numero_acidentes+ numero_cidades_2000_veiculos
    media_carros_cidades_2000 = somatoria_veiculos_cidades / numero_cidades_2000_veiculos
  

print('A cidade com maior casos de acidentes é:',cidade_maior_casos_acidentes,'. A quantidade de acidentes foi de: ',maior_casos_acidentes)
print('A cidade com menor casos de acidentes é:',cidade_menor_casos_acidentes,'. A quantidade de acidentes foi de:',menor_casos_acidentes)
print("Total de veiculos somados na pesquisa é:",somatoria_veiculos_cidades)
print("A média de veiculos é:",media_carros_cidades)
print("A média de acidentes em cidades com menos de 2000 veiculos é:",media_carros_cidades_2000)