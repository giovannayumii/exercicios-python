print("5) Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, sendo que a maioridade é obtida após completar 18 anos.")

cont_pessoas = 0

for qpessoas in range(10):   

    idade = int(input('Informe a idade: '))

    if idade >= 18:

        cont_pessoas = cont_pessoas + 1

print('Quantidade de pessoas maior de idade:',cont_pessoas)