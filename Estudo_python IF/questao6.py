num1 = int(input("digite primeiro numero"))
num2 = int(input("digite segundo numero"))
num3 = int(input("digite terceiro numero"))

if num1 > num2 and num1 > num3:
    print("numero:",num1,"e o maior numero")
if num2 > num1 and num2 > num3:
    print("numero:",num2,"e o maior numero")

if num3 > num2 and num3 > num1:
    print("numero:",num3,"e o maior numero")

if num1 == num2:
    print("numeros iguais, digite numeros diferentes")