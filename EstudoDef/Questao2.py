#1
   # 1   2
    #1   2   3
    #.....
 #   1   2   3   ...  n

def linha(numero):
    for i in range(1,numero + 1):  
       print((' {} ').format(i), end='')
    print()

def seq(numero):
    for numero in range(numero + 1):
        linha(numero)

numero = int(input("Digite um número: "))
seq(int(numero))
