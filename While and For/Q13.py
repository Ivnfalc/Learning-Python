#Faça um programa que leia um numero de 0 a 10 e informe qual produto se encontra no numero



produto = [" ", "Arroz", "Feijao", "carne", "farinha", "leite", "açucar", "adoçante", "chocolate", "agua","tempero" ]
num = []

print("informe o numero:")
for i in produto:
    num = int(input(" "))
    num = produto[num]
    break


print(num)
