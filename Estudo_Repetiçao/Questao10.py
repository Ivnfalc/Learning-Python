#Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.


num = []

print ( "informe os 10 numeros:")
for x in range (10):
    num.append(input('numero' + str(x+1) + ':\n' ))
    num.reverse()

print(num)