#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("digite M para matutino, V para vespertino e N para noturno:")


if turno ==  "m":
    print("Bom Dia!")
elif turno ==  "v":
    print("Boa tarde!")
elif turno ==  "n":
    print("Boa noite!")

else:
    print("Valor invalido")