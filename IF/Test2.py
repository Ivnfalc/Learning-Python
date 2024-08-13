#faça um programa que peça o metodo de calculo e redirecione para o calculo correto.
# exemplo: peça para usuario digitar adiçao , faça um calculo de adiçao  e mostre o resultado.

tipo = input("digite a para adição, s para subtração, d para divisao, m para multiplicação:")
num1 = float(input("digite o primeiro numero:"))
num2 = float(input("digite o segundo  numero:"))
rtad = 0

if tipo == "a":
    rtad = (num1 + num2)
    print( "resultado:",rtad )

if tipo == "s":
    rtad = (num1 - num2)
    print( "resultado:",rtad )

if tipo == "d":
    rtad = (num1 / num2)
    print("resultado:", rtad)

if tipo == "m":
    rtad = (num1 * num2)
    print("resultado:", rtad)
