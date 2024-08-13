#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão)

num = int(input("Digite numero:"))

if num % 2 == 0:
    print("numero é um valor par")
else:
    print("numero tem valor impar")