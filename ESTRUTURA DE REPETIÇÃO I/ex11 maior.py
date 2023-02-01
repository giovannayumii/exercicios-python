print("11) Construir um algoritmo que, dado o valor de 10 preços de TV, determine e apresente o valor mais caro e mais barato entre eles.")

cont = 0
while cont <= 10:
    preco = float(input('Digite o preço da TV: '))
    if cont == 0: # este if é utilizado para apenas uma vez inicializar as variáveis de resposta do exercício, caro e barato
        caro = preco 
        barato = preco
    elif preco >= caro:
        caro = preco
    elif preco <= barato :
        barato = preco
    cont = cont + 1
print('O valor mais caro é:',caro)

print('O valor mais barato é:',barato)