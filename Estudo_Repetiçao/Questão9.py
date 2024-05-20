#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

num = []

print ( "informe os 5 numeros:")
for x in range (5):
    num.append(input('numero' + str(x+1) + ':\n' ))
    num.sort()

print(num)
