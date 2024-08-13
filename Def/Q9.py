#programa que ao digitar um numero verifique se ele é par ou impar, utilizando def

def numero(num):
    if num % 2 ==0:
        return "Numero Par"
    else:
        return "numero impar"
    

num1 = int(input("digite um numero:"))
num2 = int(input("digite um numero:"))

print(f"O primeiro número é {numero(num1)}.")
print(f"O segundo número é {numero(num2)}.")
