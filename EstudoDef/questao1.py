#Faça um programa para imprimir:
   # 1
   # 2   2
   # 3   3   3
   # n   n   n   n   n   n  ... n 
    
def numero(n):
    for i in range(n):
        i += 1
        print(str(i) * i)
        


n = int(input('Digite um número: '))
numero(n)
