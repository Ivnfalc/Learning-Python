#indexing string

mystring = ("hello world")
letter = "A"
x = "my world"
result = 100/777

print(" nome e:", mystring)
print("exemplo de index normal:",mystring[4])
print("exemplo index negativo",mystring[-1]) #o -1 serve para pegar a ultima letra, independente do tamanho da string
print("exemplo index exclude" ,mystring[1:])
#index exclude, printa toda a frase excluindo a letra correspondete ao numero nesse exemplo excluiu se apenas a 1º letra
print("exemplo index exclude" ,mystring[5:])
#o efeito contrario acontece quando e comocado :5 como o exemplo abaixo:
print("exemplo index include" ,mystring[:5])
#exemplo de pulo de string:
print("exemplo index jump" ,mystring[::2])# o primeiro : significado começo o segundo : significa ate o fim
# o numero  significa o pulo.entao do começo ate o final pule 2 e entao pegue o proximo.
#isso pode ser incluido negativamente, para a frase ficar invertida, exemplo abaixo:
print("exemplo index jump invertido" ,mystring[::-1])
print(mystring + " its cold outside" ) #exemplo de string addition
print("exemplo de multiplicaçao string", letter * 10)
print("exemplo de manipulaçao string com upercase:",x.upper())
print("exemplo de manipulaçao string com list:",x.split())# no split(),pode ser colocado uma letra, essa letra será removida
print('this is a string {}'.format('INSERT')) #exemplo de insert de strin
print("the {3} {2} {0} {1} ".format("yiff","botton","is","fox"))#exeplo de list include,que pode ser organizado de acordo
#com as celulas de 0 ate 3
print("resultado foi {r:1.3f}".format(r=result))#exemplo de insert com numero float.onde o r e resultado,
#o 1.3f e o level de precisao, por exemplo vai so mostrar os 3 digitos deppois do ponto.