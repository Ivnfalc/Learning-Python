#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


n1 = int(input("digite uma nota:"))
n2 = int(input("digite uma nota:"))
n3 = int(input("digite uma nota:"))
n4 = int(input("digite uma nota:"))
media = 0 

for i in range (1,5):
    i =+ 1
    media =(n1+n2+n3+n4)/4
    
if media < 7.00:
    print ("Me desculpe, é preciso ter uma media maior que 7 para aprovação")
        
print("nota 1:", n1)
print("nota 2:", n2)
print("nota 3:", n3)
print("nota 4:", n4)
print("soma das notas:",n1 + n2 + n3 + n4)
print("media das notas:",(n1+n2+n3+n4)/4)
