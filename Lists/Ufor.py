numlist = [1,2,3,4,5,6,7,8,9,10]
somalist = 0
mylist = [(1,2),(3,4),(5,6),(7,8)]
mylist2 = [(1,2,3),(5,6,7),(8,9,0,)]
d = {'k1':1,'k2':2,'k3':3 }
for num in numlist:
    print(num,"*",numlist)

#separando numeros:
for num in numlist:
    if num % 2 == 0:
        print("numero par:",num)
    else:
        print(f'numero impar: {num}')

#execuçao da variavel somalist
for num in numlist:
    somalist = somalist + num
    print(somalist)#dentro  da identaçao do for , ira ver todos os resultados
print("resultado unico:",somalist,'\n')#fora do loop ira so ver o resultado final

#manipulando string com for
for letra in "hello world":
    print(letra,)

#execuçao com lista tuples:
print("loop com tuples:\n")
for item in mylist:
    print(item)

print("loop com tuples 2 :\n")
for (a,b) in mylist:
    print(b)

print("loop com tuples 3 :\n")
for a,b,c in mylist2:
    print(b)

print("loop com dicionario :\n")
#for loop com dicionarios:
for key,value in d.items():
    print(value)