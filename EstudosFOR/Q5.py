#Altere o programa anterior permitindo ao
# usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação



while True:
    pa = float(input('População país A: '))
    taxa1 = float(input('Taxa de crescimento país A: '))
    pb= float(input('População país B: '))
    taxa2 = float(input('Taxa de crescimento país B: '))
    x = 0

    while pa <= pb:
        x+= 1
        pa += (pa * taxa1)/100
        pb += (pb * taxa2)/100

    print("Ano:",x, "População A:", pa, "população B:",pb)

    break