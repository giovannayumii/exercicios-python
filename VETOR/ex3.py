print("3) Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a pessoa mais gorda e mais magra e apresente o nome o peso das mesmas.​ Use dois vetores, um para peso e outro para nome")

nome=[]
peso=[]
magro=0
gordo=0
for elemento in range(10):
    nome.append(input('Informe o nome: '))
    peso.append(float(input('Informe o peso: ')))
    if elemento == 0:
        gordo = peso[elemento]
        nome_gordo = nome[elemento]
        magro = peso[elemento]
        nome_magro = nome[elemento]
    if peso[elemento] >= gordo:
        gordo = peso[elemento]
        nome_gordo = nome[elemento]
    elif peso[elemento] <= magro:
        magro = peso[elemento]
        nome_magro = nome[elemento]
    elemento = elemento + 1
print('A/O ',nome_magro,'tem ',magro,'kg')
print('A/O ',nome_gordo,'tem ',gordo,'kg')