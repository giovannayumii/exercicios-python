print("7)  Faça um algoritmo que calcule e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra:\t Salário até 300, reajuste de 50%;\t Salários maiores que 300, reajuste de 30%.")

cont=1
while cont <=10:
  print("Digite o salário do funcionario:")
  salario=float(input())
  if salario <= 300:
    salario_reajustado=salario+salario*(50/100)
    print("Salário reajustado: R$ %.2f"%salario_reajustado)
  else:
    salario_reajustado=salario+salario*(30/100)
    print("Salário reajustado: R$ %.2f"%salario_reajustado)
  cont=cont+1