print("5) Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições")

n=[]
par=0

for i in range(8):
    n.append(int(input('Digite um número inteiro e positivo: ')))
for i in range(8):
    if n[i] % 2 == 0:
        par = par + 1
        print('Posição:',i,', número:',n[i])
    
print("Quantidade de números pares: ",par)
 