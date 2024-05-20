# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
som =0
mult = 0

for i in range (1,50,2):
    print("numeros impares:",i, end=" ")
    if i %2 == 1:
        som = i + i
        mult = i * i
        print("resultado quando somado por ele mesmo =",som,"quando multiplicado por ele mesmo=",mult)
