#estudo de funçao  utilizando touples unpacking
'''
stockprices = [('apple',200),('docker',200),('linux',200)]

for ticker,price  in stockprices:#o ticker serve pra apenas vc querer saber o nome 
    #isso estará dando unpacking separadamente nos items
     
    print(ticker)
    print(price +(0.1*price))#isso estará fazendo com que o print mostre o preço apenas, 
    #adicionado 10% do valor. 
    '''


whoras = [('Natty',200),('Brus',400),('ldujs',100)]

def checklist(horas):
    currentmax=0
    empregadomes = ''
    for empregado,horas in whoras:
        if horas >currentmax:
            currentmax = horas
            empregadomes = empregado
        else:
            pass

    
    return (empregadomes,currentmax)#isso vai informar qual sera o empregado do mes
    #baseado na maxima hora.

print(checklist(whoras))