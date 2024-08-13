#4) Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.


letlist=[]
conso=0

print("informa:")
for i in range (10):
    letlist.append((input('caractere' + str(i+1) + ':\n' )))
    char = letlist[i]
    if (char not in ('a','e','i','o','u')):
        conso =+1

print(conso)
