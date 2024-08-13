'''
def myfunc(*args):
    for item in args:
        print (item)
    #o *args retorna um tuple
#com a funçao *args ,pode se adicionar quantos numeros quiser, sem precisar declarar a variavel
num = int(input("numero:"))
myfunc(num * 0.05)
'''
'''
def myfun(**kwargs):#**kwargs servem para que seja feito um dictionary 
    if 'fruit' in kwargs:
        print ('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruits here')
myfun(fruit='apple',veggie='lettuce')#e assim returna um dictionary
'''
'''
#função map(lambda) serve para executar a lista de codigos uma so vez, nao amarzenando.
nums= int(input())
double = (map(lambda x:x * 2,nums)) 

print(double(5))

#seria a mesma coisa do codigo:
#def double(x):
       #return x * 2

'''


