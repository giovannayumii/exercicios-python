print("15) Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.")

numero_de_elementos_da_sequencia = 8
elementoN = 0
elementoNmais1 = 1
 
print("%d"%elementoN)
print("%d"%elementoNmais1)
 
for elemento in range (3,8):
  valor_do_fibonacci_atual = elementoN + elementoNmais1
  print("%d"%valor_do_fibonacci_atual)
 
  elementoN = elementoNmais1
  elementoNmais1 = valor_do_fibonacci_atual