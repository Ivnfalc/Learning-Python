#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nlist = []
media = 0


print("informe as notas:")
for i in range (4):
    nlist.append(float(input('Nota ' + str(i + 1) + ':\n')))
    media = nlist[i]
media = media /4
print(nlist)
print("media:",media)