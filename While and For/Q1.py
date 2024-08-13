#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
numero = 0


while True:
    numero = int(input("digite nota:"))
    if numero > 10 or numero < 0:
        print("invalid number")
        continue
    else:
        break
