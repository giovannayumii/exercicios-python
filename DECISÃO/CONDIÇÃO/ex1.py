print("1) aça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 500, reajuste de 50%; Salários maiores que 500, reajuste de 30%.")

salario = float(input('Informe o salário: '))
if salario <= 500:
    reajuste = salario + salario * 50 / 100
else:
    reajuste = salario + salario * 30 / 100
print('Novo salario=',reajuste)