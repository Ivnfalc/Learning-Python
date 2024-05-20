#faça um programa para identificar produtos e identique o preço das mesmas.


produtos = [{"mesa":333.00},{"cadeira":188.00},{"fogão":500.00},{"geladeira":903.00}]



for x in produtos:
    i = input("digite produto:")
    print("Preço:","R$",x[i])