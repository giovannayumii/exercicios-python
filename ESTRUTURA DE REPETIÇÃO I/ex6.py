print("6) Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares.")

cont = 0
par = 0
impar = 0
for cont in range (23):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        num = par
        par = par +1
    else: 
        num = impar
        impar = impar + 1
print("Há %d números pares "%par)
print("Há %d números impares"%impar) 
