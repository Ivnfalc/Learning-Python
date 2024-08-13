#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

num1 = int(input("numero:"))
num2 = 0

n1list = []
 
for num1 in range (0,num1):
    
    n1list.append(num1)
    n1list.append(num2)
    num1 = num1 + 1  
    num2 = num1 + num1 -1
    print(num1,"/",num2)

