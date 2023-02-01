print("13) 14. Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que: \t Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.\t Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.\t A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.\tFaça um programa que determine o salário atual desse funcionário.")

print("Digite o ano atual")
ano_atual=int(input())
salario_inicial =1000
percentual_de_aumento_do_ano  = 1.5 / 100
aumento_do_ano = salario_inicial * percentual_de_aumento_do_ano
salario_do_ano = salario_inicial + aumento_do_ano
percentual_do_ano=percentual_de_aumento_do_ano
for ano in range(2007,2010):
  percentual_do_ano=percentual_do_ano*2
  aumento_do_ano = salario_do_ano * percentual_do_ano
  salario_do_ano = salario_do_ano + aumento_do_ano
print("Ano: %d, salário a receber esse ano: R$%.2f"%(ano_atual,salario_do_ano))