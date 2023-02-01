print("8) Faça um algoritmo que conheça 4 valores diferentes, some-os e mostre o resultado.")

soma_numeros = 0
contador = 0

while contador < 4: # for contador in range(4):

    num = int(input('Informe um valor: '))  

    soma_numeros = soma_numeros + num

    contador = contador + 1

print('Valor somado', soma_numeros)