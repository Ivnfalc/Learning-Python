#o usuario deve digitar um numero ,e no final deve mostrar se o num e par ou impar.
while True:
    numero = int(input("digite um numero:"))
    if numero % 2 == 0:
        print(numero, "numero e par")

    else:
        print("numero impar")
