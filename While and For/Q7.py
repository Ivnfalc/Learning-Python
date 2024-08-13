#faça um programa que calcule uma quantidade determinada de numeros.
#no final, mostre o resultado da soma, divisao ,e o maior numero digitado.
i = 0
soma = 0
t = 0
div = 0
maior = 0

while i == 0:
    num = int(input("digite numero:"))
    i = i + 1
    num2 = int(input("digite numero:"))
    soma = num + num2
    t = soma
    div = (soma /t)
if num > num2:
    maior = num
else:
    maior = num2

print("soma:", soma)
print("divisão:" ,div)
print( "Maior numero:", maior)