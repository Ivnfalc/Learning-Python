#estudo sobre funçao def usando logics

'''
def func(num):
    result = num % 2 == 0
    print(func) #vai retornar verdadeiro somente se o numero do print func for com resto zero
    na divisão 
    return result

print (func(20))
'''
'''

def checklist(numlist):
    for number in numlist:
        if number % 2 == 0:
            return True #retornará True se existir um numero na lista que par
        else:
            pass 
    return False #o return false deve ser finalizando o for loop, pois se estiver dentro do
    #if statement,ira sempre dar false.

print (checklist[1,3,2])#se o numero for par retorna'verdadeiro

'''

even_numbers = [] #para retornar todos os even numbers da list e se nao existir, retornar vazio.

def checklist(numlist):
    for number in numlist:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass 
    return even_numbers
print(checklist[1,2,3,4,5]) #vai  retornar apenas o 2 e 4