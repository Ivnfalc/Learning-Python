#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("digite o valor do produto:"))

prod2 = float(input("digite o valor do produto:"))

prod3 = float(input("digite o valor do produto:"))

if prod1 > prod2 or prod1 > prod3:
    print("produto 1 tem o valor alto")
else:
    print("produto 1 tem o valor mais baixo, deve se comprar esse")
if prod2 > prod1 or prod2 > prod3:
    print("produto 2 tem o valor alto")
else:
    print("produto 2 tem o valor mais baixo, deve se comprar esse")
if prod3 > prod1 or prod3 > prod2:
    print("produto 3  tem o valor alto")
else:
    print("produto 3 tem o valor mais baixo, deve se comprar esse ")