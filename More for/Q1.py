#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = -1


while nota < 0 or nota > 10:
    nota = int(input('Nota de 0 a 10: '))
    if nota > 10 or nota < 0:
        print("Nota invalida , Digite uma nota entre 0 ate 10")