#Faça um Programa que peça dois números e imprima o maior deles

num1= int(input("digite primeiro numero"))
num2= int(input("digite segundo numero"))


if num1 > num2:
    print("numero:",num1,"e o maior numero")
if num2 > num1:
    print("numero:",num2,"e o maior numero")
if num1 == num2:
    print("numeros iguais, digite numeros diferentes")