#Faça um programa, com uma função que necessite de um argumento.
#  A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

def farg(numero):
    if numero > 0: 
        print("positivo")
    elif numero == 0:
        print("nulo")

    else:
        print("negativo")


print('POSITIVO OU NEGATIVO')
numero = int(input('digite um número: '))
print('Este número é', end=' ')
farg(numero)
